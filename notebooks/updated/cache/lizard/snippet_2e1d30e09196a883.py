def log(function):

    def _log(self, *args, **kwargs):
        ret = function(self, *args, **kwargs)
        if len(self.history) > self.maxHistory:
            self.history = self.history[1:self.maxHistory]
        self.history.append({'errorMsg': self.errorMsg, 'payload': self.
            payload, 'url': self.url, 'resp': self.resp, 'res': self.res,
            'printErrors': self.printErrors, 'method': self.method})
        self.clearReqVars()
        return ret
    return _log