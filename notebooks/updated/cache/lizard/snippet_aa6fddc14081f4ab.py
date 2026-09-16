def refund(self, amount=None, reason=None):
    charge_obj = self.api_retrieve().refund(amount=self.
        _calculate_refund_amount(amount=amount), reason=reason)
    return self.__class__.sync_from_stripe_data(charge_obj)