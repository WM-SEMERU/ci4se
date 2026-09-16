def verify_order(self, **kwargs):
    create_options = self._generate_create_dict(**kwargs)
    return self.client['Product_Order'].verifyOrder(create_options)