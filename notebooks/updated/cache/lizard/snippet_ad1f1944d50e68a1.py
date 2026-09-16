def start_datafeed(self, datafeed_id, body=None, params=None):
    if datafeed_id in SKIP_IN_PATH:
        raise ValueError(
            "Empty value passed for a required argument 'datafeed_id'.")
    return self.transport.perform_request('POST', _make_path('_ml',
        'datafeeds', datafeed_id, '_start'), params=params, body=body)