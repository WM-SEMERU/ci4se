def get_exchange_rates(self, base, targets=None):
    if targets is None:
        targets = get_available_currencies()
    return {t: self.get_exchange_rate(base, t, raise_errors=False) for t in
        targets}