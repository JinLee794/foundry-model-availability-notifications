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

    const dt = table.DataTable({
      pageLength: 25,
      lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
      order: [],
      dom: 'Blfrtip',
      buttons: [
        {
          extend: 'colvis',
          text: 'Columns',
          className: 'btn-column-visibility'
        }
      ],
      language: {
        search: "Search:",
        lengthMenu: "Show _MENU_ entries",
        info: "Showing _START_ to _END_ of _TOTAL_ entries",
        infoFiltered: "(filtered from _MAX_ total entries)"
      },
      initComplete: function() {
        // Add column filters for specific columns
        this.api().columns().every(function() {
          const column = this;
          const header = $(column.header());
          const filterType = header.data('filter');
          
          if (filterType === 'select') {
            const select = $('<select class="column-filter"><option value="">All</option></select>')
              .appendTo($(column.footer()).empty())
              .on('change', function() {
                const val = $.fn.dataTable.util.escapeRegex($(this).val());
                column.search(val ? '^' + val + '$' : '', true, false).draw();
              });

            column.data().unique().sort().each(function(d) {
              // Strip HTML tags for option text
              const text = $('<div>').html(d).text().trim();
              if (text) {
                select.append('<option value="' + text + '">' + text + '</option>');
              }
            });
          }
        });
      }
    });
  });

  // Custom filter handlers for SKU type filtering
  window.filterBySku = function(skuType) {
    const table = $('#availability-table').DataTable();
    if (skuType === 'all') {
      table.column(3).search('').draw();
    } else {
      table.column(3).search(skuType).draw();
    }
  };

  // Custom filter handlers for region filtering
  window.filterByRegion = function(region) {
    const table = $('#availability-table').DataTable();
    if (region === 'all') {
      table.column(4).search('').draw();
    } else {
      table.column(4).search(region).draw();
    }
  };

  // Custom filter handlers for coverage level
  window.filterByCoverage = function(coverage) {
    const table = $('#availability-table').DataTable();
    if (coverage === 'all') {
      table.column(1).search('').draw();
    } else {
      table.column(1).search(coverage).draw();
    }
  };

  // Reset all filters
  window.resetFilters = function() {
    const table = $('#availability-table').DataTable();
    table.search('').columns().search('').draw();
    
    // Reset select elements
    $('.filter-controls select').val('all');
  };
});

// Re-initialize tables when page changes (for MkDocs instant navigation)
if (typeof document$ !== 'undefined') {
  document$.subscribe(function() {
    if (typeof jQuery !== 'undefined' && jQuery.fn.DataTable) {
      jQuery('.filterable').each(function() {
        if (!jQuery.fn.DataTable.isDataTable(this)) {
          jQuery(this).DataTable({
            pageLength: 25,
            lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
            order: [],
            dom: 'Blfrtip'
          });
        }
      });
    }
  });
}
