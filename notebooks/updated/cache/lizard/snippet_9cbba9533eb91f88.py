def _fetch(self, params, required, defaults):
    defaults.update(params)
    pp_params = self._check_and_update_params(required, defaults)
    pp_string = self.signature + urlencode(pp_params)
    response = self._request(pp_string)
    response_params = self._parse_response(response)
    log.debug('PayPal Request:\n%s\n', pprint.pformat(defaults))
    log.debug('PayPal Response:\n%s\n', pprint.pformat(response_params))
    nvp_params = {}
    tmpd = defaults.copy()
    tmpd.update(response_params)
    for k, v in tmpd.items():
        if k in self.NVP_FIELDS:
            nvp_params[str(k)] = v
    if 'timestamp' in nvp_params:
        nvp_params['timestamp'] = paypaltime2datetime(nvp_params['timestamp'])
    nvp_obj = PayPalNVP(**nvp_params)
    nvp_obj.init(self.request, params, response_params)
    nvp_obj.save()
    return nvp_obj