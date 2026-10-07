---
hide:
  - navigation
  - toc
search:
  exclude: true
---

# By SKU Type has moved

<p class="page-lede">This view is now part of the <a href="../explorer/">Availability Explorer</a>, which shows every model, region and deployment type in one grid.</p>

<p><a class="md-button md-button--primary" href="../explorer/">Open the Availability Explorer</a></p>

<script>
(function () {
  var value = new URLSearchParams(location.search).get('sku');
  var map = {"Datazone Provisioned Managed Gov":"dp","Datazone Standard Gov":"dz","Datazone Standard Priority Processing":"dz","Datazone provisioned managed":"dp","Datazone standard":"dz","Deployments Batch":"bt","Deployments Provisioned":"rp","Deployments Standard":"rs","Global Standard":"gs","Global batch":"bt","Global batch datazone":"bt","Global coverage":"gs","Marketplace Deployments Standard":"mp","Provisioned (PTU managed)":"rp","Provisioned Models Gov":"rp","Provisioned global":"gp","Region Availability Maas":"mp","Standard":"rs","Standard Global By Capability":"gs","Standard Global Priority Processing":"gs","Standard Models Gov":"rs"};
  var hash = '';
  if (value) hash = map[value] ? '#t=' + map[value] : '';
  location.replace('../explorer/' + hash);
})();
</script>
