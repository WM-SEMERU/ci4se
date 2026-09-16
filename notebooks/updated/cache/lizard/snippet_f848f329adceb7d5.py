def ledger(self, ledger_id):
    endpoint = '/ledgers/{ledger_id}'.format(ledger_id=ledger_id)
    return self.query(endpoint)