def _make_proxy(self, varname, parent=None, constructor=MlabObjectProxy):
    proxy_val_name = 'PROXY_VAL%d__' % self._proxy_count
    self._proxy_count += 1
    mlabraw.eval(self._session, '%s = %s;' % (proxy_val_name, varname))
    res = constructor(self, proxy_val_name, parent)
    self._proxies[proxy_val_name] = res
    return res