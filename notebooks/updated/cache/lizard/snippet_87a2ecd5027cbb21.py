def get_order_history(self, market=None):
    if market:
        return self._api_query(path_dict={API_V1_1:
            '/account/getorderhistory', API_V2_0:
            '/key/market/GetOrderHistory'}, options={'market': market,
            'marketname': market}, protection=PROTECTION_PRV)
    else:
        return self._api_query(path_dict={API_V1_1:
            '/account/getorderhistory', API_V2_0:
            '/key/orders/getorderhistory'}, protection=PROTECTION_PRV)