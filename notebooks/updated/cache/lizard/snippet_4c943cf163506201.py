def _get_balance(self, account_number):
    data = {'ctn': self.username, 'language': 'en-US', 'accountNumber':
        account_number}
    try:
        raw_res = yield from self._session.post(BALANCE_URL, data=data,
            headers=self._headers, timeout=self._timeout)
    except OSError:
        raise PyFidoError('Can not get balance')
    try:
        json_content = yield from raw_res.json()
        balance_str = json_content.get('getAccountInfo', {}).get('balance')
    except (OSError, ValueError):
        raise PyFidoError('Can not get balance as json')
    if balance_str is None:
        raise PyFidoError('Can not get balance')
    try:
        balance = float(balance_str)
    except ValueError:
        raise PyFidoError('Can not get balance as float')
    return balance