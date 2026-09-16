def list_market_profit_and_loss(self, market_ids, include_settled_bets=
    False, include_bsp_bets=None, net_of_commission=None):
    return self.make_api_request('Sports', 'listMarketProfitAndLoss', utils
        .get_kwargs(locals()), model=models.MarketProfitAndLoss)