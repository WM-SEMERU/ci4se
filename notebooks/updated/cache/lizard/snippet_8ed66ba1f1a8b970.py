def set_vads_payment_config(self):
    self.vads_payment_config = tools.get_vads_payment_config(self.
        payment_config, self.custom_payment_config.all())