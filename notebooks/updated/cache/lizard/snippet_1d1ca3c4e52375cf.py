def update_recurring_payments_profile(self, profileid, **kwargs):
    kwargs.update(self._sanitize_locals(locals()))
    return self._call('UpdateRecurringPaymentsProfile', **kwargs)