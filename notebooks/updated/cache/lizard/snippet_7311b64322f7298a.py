def validate_params(self, params):
    plen = 0
    if params != None:
        plen = len(params)
    if len(self.params) != plen:
        vals = self.full_name, len(self.params), plen
        msg = "Function '%s' expects %d param(s). %d given." % vals
        raise RpcException(ERR_INVALID_PARAMS, msg)
    if params != None:
        i = 0
        for p in self.params:
            self._validate_param(p, params[i])
            i += 1