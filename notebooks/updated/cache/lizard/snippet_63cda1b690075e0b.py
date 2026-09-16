def getcomponents(self, product, force_refresh=False):
    proddict = self._lookup_product_in_cache(product)
    product_id = proddict.get('id', None)
    if (force_refresh or product_id is None or product_id not in self.
        _cache.component_names):
        self.refresh_products(names=[product], include_fields=['name', 'id'])
        proddict = self._lookup_product_in_cache(product)
        if 'id' not in proddict:
            raise BugzillaError("Product '%s' not found" % product)
        product_id = proddict['id']
        opts = {'product_id': product_id, 'field': 'component'}
        names = self._proxy.Bug.legal_values(opts)['values']
        self._cache.component_names[product_id] = names
    return self._cache.component_names[product_id]