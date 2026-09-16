def set_monthly_billing(self, currency, client_pays, markup_percentage,
    monthly_scheme=None):
    body = {'Currency': currency, 'ClientPays': client_pays,
        'MarkupPercentage': markup_percentage}
    if monthly_scheme is not None:
        body['MonthlyScheme'] = monthly_scheme
    response = self._put(self.uri_for('setmonthlybilling'), json.dumps(body))