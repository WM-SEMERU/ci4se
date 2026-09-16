def setSpecialPrice(self, product, special_price=None, from_date=None,
    to_date=None, store_view=None, identifierType=None):
    return bool(self.call('catalog_product.setSpecialPrice', [product,
        special_price, from_date, to_date, store_view, identifierType]))