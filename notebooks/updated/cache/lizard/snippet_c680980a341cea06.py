def get_account_statement(self, locale=None, from_record=None, record_count
    =None, item_date_range=time_range(), include_item=None, wallet=None,
    session=None, lightweight=None):
    params = clean_locals(locals())
    method = '%s%s' % (self.URI, 'getAccountStatement')
    response, elapsed_time = self.request(method, params, session)
    return self.process_response(response, resources.AccountStatementResult,
        elapsed_time, lightweight)