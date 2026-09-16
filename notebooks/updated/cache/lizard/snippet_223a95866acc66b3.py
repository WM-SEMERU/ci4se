def get_address(self, address):
    params = self.build_basic_request()
    params['address'] = address
    response = util.call_api('merchant/{0}/address_balance'.format(self.
        identifier), params, base_url=self.service_url)
    json_response = json.loads(response)
    self.parse_error(json_response)
    return Address(json_response['balance'], json_response['address'], None,
        json_response['total_received'])