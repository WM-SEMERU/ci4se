def set_stable_spot_instance_settings(self, maximum_bid_price_percentage=
    None, timeout_for_request=None, allow_fallback=True):
    self.hadoop_settings['stable_spot_instance_settings'] = {
        'maximum_bid_price_percentage': maximum_bid_price_percentage,
        'timeout_for_request': timeout_for_request, 'allow_fallback':
        allow_fallback}