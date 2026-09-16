def get_market_history(self, market):
    return self._api_query(path_dict={API_V1_1: '/public/getmarkethistory'},
        options={'market': market, 'marketname': market}, protection=
        PROTECTION_PUB)