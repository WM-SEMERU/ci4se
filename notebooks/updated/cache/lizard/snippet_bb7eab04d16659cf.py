def set_address(self, address):
    self._query_params += str(QueryParam.ADVANCED) + str(QueryParam.ADDRESS
        ) + address.replace(' ', '+').lower()