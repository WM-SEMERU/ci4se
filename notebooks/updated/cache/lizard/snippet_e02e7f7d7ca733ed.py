def _calculate_order_value_amount(self, asset, value):
    if not self.executor.current_data.can_trade(asset):
        raise CannotOrderDelistedAsset(msg=
            'Cannot order {0}, as it not tradable'.format(asset.symbol))
    last_price = self.executor.current_data.current(asset, 'price')
    if np.isnan(last_price):
        raise CannotOrderDelistedAsset(msg=
            'Cannot order {0} on {1} as there is no last price for the security.'
            .format(asset.symbol, self.datetime))
    if tolerant_equals(last_price, 0):
        zero_message = "Price of 0 for {psid}; can't infer value".format(psid
            =asset)
        log.debug(zero_message)
        return 0
    return value / last_price