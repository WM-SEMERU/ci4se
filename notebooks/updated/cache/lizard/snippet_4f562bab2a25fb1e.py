def create(self, product, data, store_view=None, identifierType=None):
    return self.call('catalog_product_attribute_media.create', [product,
        data, store_view, identifierType])