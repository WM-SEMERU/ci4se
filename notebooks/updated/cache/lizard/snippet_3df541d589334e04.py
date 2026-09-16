def campaign_name(self, campaign_name):
    if campaign_name is None:
        raise ValueError(
            'Invalid value for `campaign_name`, must not be `None`')
    if campaign_name is not None and len(campaign_name) > 250:
        raise ValueError(
            'Invalid value for `campaign_name`, length must be less than or equal to `250`'
            )
    if campaign_name is not None and len(campaign_name) < 1:
        raise ValueError(
            'Invalid value for `campaign_name`, length must be greater than or equal to `1`'
            )
    self._campaign_name = campaign_name