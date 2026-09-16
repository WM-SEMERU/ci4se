def get_account_activity(self, account_id, start=None, end=None, page=None,
    limit=None):
    data = {}
    if start:
        data['startAt'] = start
    if end:
        data['endAt'] = end
    if page:
        data['currentPage'] = page
    if limit:
        data['pageSize'] = limit
    return self._get('accounts/{}/ledgers'.format(account_id), True, data=data)