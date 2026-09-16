def get_account_details(self, session=None, lightweight=None):
    params = clean_locals(locals())
    method = '%s%s' % (self.URI, 'getAccountDetails')
    response, elapsed_time = self.request(method, params, session)
    return self.process_response(response, resources.AccountDetails,
        elapsed_time, lightweight)