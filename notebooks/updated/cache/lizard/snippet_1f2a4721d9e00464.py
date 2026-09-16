def load_product_object(self, name):
    product_entry = self.products[name]
    product = self._get_base_object(product_entry)
    return product