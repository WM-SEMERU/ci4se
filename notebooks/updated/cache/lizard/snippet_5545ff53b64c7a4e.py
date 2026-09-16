def setExpressCheckout(self, params):
    if self._is_recurring(params):
        params = self._recurring_setExpressCheckout_adapter(params)
    defaults = {'method': 'SetExpressCheckout', 'noshipping': 1}
    required = ['returnurl', 'cancelurl', 'paymentrequest_0_amt']
    nvp_obj = self._fetch(params, required, defaults)
    if nvp_obj.flag:
        raise PayPalFailure(nvp_obj.flag_info, nvp=nvp_obj)
    return nvp_obj