// Fullscreen toggle functionality
(function() {
  function createFullscreenToggle() {
    // Don't create if already exists
    if (document.getElementById('fullscreen-toggle-btn')) return;
    
    const btn = document.createElement('button');
    btn.id = 'fullscreen-toggle-btn';
    btn.className = 'fullscreen-toggle';
    btn.title = 'Toggle fullscreen mode';
    btn.innerHTML = `
      <svg class="expand-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
      </svg>
      <svg class="collapse-icon" style="display:none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/>
      </svg>
    `;
    
    btn.addEventListener('click', function() {
      document.body.classList.toggle('fullscreen-mode');
      const isFullscreen = document.body.classList.contains('fullscreen-mode');
      
      // Toggle icons
      btn.querySelector('.expand-icon').style.display = isFullscreen ? 'none' : 'block';
      btn.querySelector('.collapse-icon').style.display = isFullscreen ? 'block' : 'none';
      
      // Update title
      btn.title = isFullscreen ? 'Exit fullscreen mode' : 'Toggle fullscreen mode';
      
      // Save preference
      localStorage.setItem('fullscreen-mode', isFullscreen ? 'true' : 'false');
      
      // Trigger resize for DataTables and recalculate columns
      window.dispatchEvent(new Event('resize'));
      
      // Recalculate DataTables columns after a short delay
      setTimeout(function() {
        if (typeof jQuery !== 'undefined' && jQuery.fn.DataTable) {
          jQuery.fn.DataTable.tables({ visible: true, api: true }).columns.adjust().draw();
        }
      }, 100);
    });
    
    document.body.appendChild(btn);
    
    // Restore saved preference
    if (localStorage.getItem('fullscreen-mode') === 'true') {
      document.body.classList.add('fullscreen-mode');
      btn.querySelector('.expand-icon').style.display = 'none';
      btn.querySelector('.collapse-icon').style.display = 'block';
      btn.title = 'Exit fullscreen mode';
    }
  }
  
  // Create on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createFullscreenToggle);
  } else {
    createFullscreenToggle();
  }
  
  // Recreate on MkDocs instant navigation
  if (typeof document$ !== 'undefined') {
    document$.subscribe(createFullscreenToggle);
  }
})();

// Initialize DataTables with filtering
document.addEventListener('DOMContentLoaded', function() {
  // Wait for jQuery and DataTables to load
  if (typeof jQuery === 'undefined') {
    console.warn('jQuery not loaded yet, retrying...');
    setTimeout(arguments.callee, 100);
    return;
  }

  const $ = jQuery;

  // Initialize all tables with the 'filterable' class
  $('.filterable').each(function() {
    const table = $(this);
    
    // Check if already initialized
    if ($.fn.DataTable.isDataTable(table)) {
      return;
    }

    table.DataTable({
      pageLength: 25,
      lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
      order: [],
      dom: 'lfrtip',
      scrollX: true,
      autoWidth: false,
      language: {
        search: "Search:",
        lengthMenu: "Show _MENU_ entries",
        info: "Showing _START_ to _END_ of _TOTAL_ entries",
        infoFiltered: "(filtered from _MAX_ total entries)"
      },
      columnDefs: [
        { targets: 'hidden-col', visible: false }
      ]
    });
  });

  // Initialize history table (simple, no row grouping)
  if ($('#history-table').length && !$.fn.DataTable.isDataTable('#history-table')) {
    $('#history-table').DataTable({
      pageLength: 50,
      lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "All"]],
      order: [[0, 'desc']],
      dom: 'lfrtip',
      language: {
        search: "Search:",
        lengthMenu: "Show _MENU_ entries",
        info: "Showing _START_ to _END_ of _TOTAL_ entries",
        infoFiltered: "(filtered from _MAX_ total entries)"
      }
    });
  }
});

// Filter function for models table (All Models page)
window.filterModelsTable = function() {
  const $ = jQuery;
  const table = $('#models-table').DataTable();

  const coverageVal = $('#coverage-filter').val() || '';
  const categoryVal = $('#category-filter').val() || '';
  const regionVal = $('#region-filter').val() || '';

  // Clear existing searches
  table.columns().search('');

  // Apply coverage filter (column 1 - Coverage)
  if (coverageVal) {
    table.column(1).search(coverageVal);
  }

  // Apply category filter (column 7 - hidden Categories)
  if (categoryVal) {
    table.column(7).search(categoryVal);
  }

  // Apply region filter (column 8 - hidden Region List)
  if (regionVal) {
    table.column(8).search(regionVal);
  }

  table.draw();
};

// Reset filters for models table
window.resetModelsFilters = function() {
  const $ = jQuery;
  const table = $('#models-table').DataTable();
  
  table.search('').columns().search('').draw();
  
  // Reset select elements
  $('#coverage-filter').val('');
  $('#category-filter').val('');
  $('#region-filter').val('');
};

// Filter function for region table (By Region page)
window.filterRegionTable = function() {
  const $ = jQuery;
  const table = $('#region-table').DataTable();
  
  const regionVal = $('#region-select').val() || '';
  const modelVal = $('#model-search').val() || '';
  const categoryVal = $('#sku-category-filter').val() || '';
  
  // Clear existing searches
  table.columns().search('');
  
  // Apply region filter (column 0 - Region)
  if (regionVal) {
    table.column(0).search('^' + regionVal.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$', true, false);
  }
  
  // Apply model search (column 1 - Model)
  if (modelVal) {
    table.column(1).search(modelVal);
  }
  
  // Apply category filter (column 2 - Categories)
  if (categoryVal) {
    table.column(2).search(categoryVal);
  }
  
  table.draw();
};

// Reset filters for region table
window.resetRegionFilters = function() {
  const $ = jQuery;
  const table = $('#region-table').DataTable();
  
  table.search('').columns().search('').draw();
  
  // Reset form elements
  $('#region-select').val('');
  $('#model-search').val('');
  $('#sku-category-filter').val('');
};

// Filter function for history table
window.filterHistoryTable = function() {
  const $ = jQuery;
  const table = $('#history-table').DataTable();
  
  const dateVal = $('#history-date-filter').val() || '';
  const typeVal = $('#history-type-filter').val() || '';
  const modelVal = $('#history-model-filter').val() || '';
  const regionVal = $('#history-region-filter').val() || '';
  const skuVal = $('#history-sku-filter').val() || '';
  
  // Clear existing searches
  table.columns().search('');
  
  // Apply date filter (column 0 - Date)
  if (dateVal) {
    table.column(0).search('^' + dateVal.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$', true, false);
  }
  
  // Apply type filter (column 1 - Change)
  if (typeVal) {
    table.column(1).search(typeVal);
  }
  
  // Apply model filter (column 2 - Model)
  if (modelVal) {
    table.column(2).search('^' + modelVal.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$', true, false);
  }
  
  // Apply region filter (column 3 - Region)
  if (regionVal) {
    table.column(3).search('^' + regionVal.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$', true, false);
  }
  
  // Apply SKU filter (column 4 - SKU Type)
  if (skuVal) {
    table.column(4).search(skuVal);
  }
  
  table.draw();
};

// Reset filters for history table
window.resetHistoryFilters = function() {
  const $ = jQuery;
  const table = $('#history-table').DataTable();
  
  table.search('').columns().search('').draw();
  
  // Reset form elements
  $('#history-date-filter').val('');
  $('#history-type-filter').val('');
  $('#history-model-filter').val('');
  $('#history-region-filter').val('');
  $('#history-sku-filter').val('');
};

// Legacy filter functions for backward compatibility
window.filterTable = window.filterModelsTable;
window.resetFilters = window.resetModelsFilters;

// Filter by clicking a region badge
window.filterByRegion = function(region) {
  const regionFilter = document.getElementById('region-filter');
  if (regionFilter) {
    regionFilter.value = region;
    filterModelsTable();
  }
};

// Helper to create a region badge HTML
function createRegionBadge(region) {
  return '<span class="region-badge" onclick="filterByRegion(\'' + region + '\')">' + region + '</span>';
}

// Toggle region badges expansion (for cells with many regions)
window.toggleRegionBadges = function(btn) {
  const span = btn.parentElement;
  const isExpanded = btn.dataset.expanded === 'true';
  const previewRegions = span.dataset.previewRegions.split(',');
  const allRegions = span.dataset.allRegions.split(',');
  
  if (isExpanded) {
    // Collapse - show preview + button
    const previewBadges = previewRegions.map(createRegionBadge).join(' ');
    const remaining = allRegions.length - previewRegions.length;
    span.innerHTML = previewBadges + ' <button class="expand-btn" onclick="toggleRegionBadges(this)">+' + remaining + ' more</button>';
  } else {
    // Expand - show all + collapse button
    const allBadges = allRegions.map(createRegionBadge).join(' ');
    span.innerHTML = allBadges + ' <button class="expand-btn" onclick="toggleRegionBadges(this)" data-expanded="true">Show less</button>';
  }
};

// Legacy toggle function
window.toggleRegions = window.toggleRegionBadges;

// Re-initialize tables when page changes (for MkDocs instant navigation)
if (typeof document$ !== 'undefined') {
  document$.subscribe(function() {
    if (typeof jQuery !== 'undefined' && jQuery.fn.DataTable) {
      var $ = jQuery;
      
      // Initialize filterable tables
      $('.filterable').each(function() {
        if (!$.fn.DataTable.isDataTable(this)) {
          $(this).DataTable({
            pageLength: 25,
            lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
            order: [],
            dom: 'lfrtip',
            scrollX: true,
            autoWidth: false,
            columnDefs: [
              { targets: 'hidden-col', visible: false }
            ]
          });
        }
      });
      
      // Initialize history table (simple, no row grouping)
      if ($('#history-table').length && !$.fn.DataTable.isDataTable('#history-table')) {
        $('#history-table').DataTable({
          pageLength: 50,
          lengthMenu: [[25, 50, 100, -1], [25, 50, 100, "All"]],
          order: [[0, 'desc']],
          dom: 'lfrtip'
        });
      }
    }
  });
}
