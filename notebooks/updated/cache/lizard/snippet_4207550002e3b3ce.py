def get_exchange_rate(self, base, target, raise_errors=True):
    assert base and target
    base, target = base.lower(), target.lower()
    r = self.session.get(API_SIMPLE_TICKER.format(base, target))
    if r.status_code != requests.codes.ok:
        if not raise_errors:
            return None
        raise CryptonatorException(
            'An error occurred while getting requested exchange rate ({} from Cryptonator).'
            .format(r.status_code))
    j = r.json()
    if not j['success'] or j['error']:
        if not raise_errors:
            return None
        raise CryptonatorException(
            "An error occurred while getting requested exchange rate ({}, {})('{}')."
            .format(base, target, j['error']))
    return float(j['ticker']['price'])