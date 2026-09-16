def request(self, result_limit, result_start, filters=None, params=None):
    return self.tc_requests.request(self.api_type, self.api_sub_type,
        result_limit, result_start, owner=self.owner, filters=filters,
        params=params)