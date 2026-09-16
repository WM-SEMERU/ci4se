def addresses(self, quote_id, address_data, store_view=None):
    return bool(self.call('cart_customer.addresses', [quote_id,
        address_data, store_view]))