def _get_params(self, rdata):
    if 'params' in rdata:
        if isinstance(rdata['params'], dict) or isinstance(rdata['params'],
            list) or rdata['params'] is None:
            return rdata['params']
        else:
            raise InvalidRequestError
    else:
        return None