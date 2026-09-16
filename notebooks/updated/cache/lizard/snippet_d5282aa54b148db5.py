def get_market_summary(self, market):
    return self._api_query(path_dict={API_V1_1: '/public/getmarketsummary',
        API_V2_0: '/pub/Market/GetMarketSummary'}, options={'market':
        market, 'marketname': market}, protection=PROTECTION_PUB)