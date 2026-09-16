def get_balance(self, asset_hash, id=None, endpoint=None):
    return self._call_endpoint(GET_BALANCE, params=[asset_hash], id=id,
        endpoint=endpoint)