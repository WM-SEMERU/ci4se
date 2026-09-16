def list_market_profit_and_loss(self, market_ids, include_settled_bets=None,
    include_bsp_bets=None, net_of_commission=None, session=None,
    lightweight=None):
    params = clean_locals(locals())
    method = '%s%s' % (self.URI, 'listMarketProfitAndLoss')
    response, elapsed_time = self.request(method, params, session)
    return self.process_response(response, resources.MarketProfitLoss,
        elapsed_time, lightweight)