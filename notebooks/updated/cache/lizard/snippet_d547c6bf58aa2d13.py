def getHTMLPopup(self, oid):
    if self.htmlPopupType != 'esriServerHTMLPopupTypeNone':
        popURL = self._url + '/%s/htmlPopup' % oid
        params = {'f': 'json'}
        return self._get(url=popURL, param_dict=params, securityHandler=
            self._securityHandler, proxy_port=self._proxy_port, proxy_url=
            self._proxy_url)
    return ''