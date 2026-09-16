def create(self, product_type, attribute_set_id, sku, data):
    return int(self.call('catalog_product.create', [product_type,
        attribute_set_id, sku, data]))