def get_supplier_properties_per_page(self, per_page=1000, page=1, params=None):
    return self._get_resource_per_page(resource=SUPPLIER_PROPERTIES,
        per_page=per_page, page=page, params=params)