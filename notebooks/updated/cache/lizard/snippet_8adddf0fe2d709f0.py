def refresh(self, asset_report_token, days_requested, options=None):
    options = options or {}
    return self.client.post('/asset_report/refresh', {'asset_report_token':
        asset_report_token, 'days_requested': days_requested, 'options':
        options})