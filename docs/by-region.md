---
hide:
  - navigation
  - toc
search:
  exclude: true
---

# By Region has moved

<p class="page-lede">This view is now part of the <a href="../explorer/">Availability Explorer</a>, which shows every model, region and deployment type in one grid.</p>

<p><a class="md-button md-button--primary" href="../explorer/">Open the Availability Explorer</a></p>

<script>
(function () {
  var value = new URLSearchParams(location.search).get('region');
  var map = {};
  var hash = '';
  if (value) hash = '#rg=' + encodeURIComponent(value);
  location.replace('../explorer/' + hash);
})();
</script>
