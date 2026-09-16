def call(self):
    headers, data = self.prepare()
    if _LOG.isEnabledFor(logging.DEBUG):
        _LOG.debug('Sending %s, %s', headers, prettify(data))
    response = requests.post(self.endpoint, headers=headers, data=data.
        encode('utf-8'), **self.request_args)
    _LOG.debug('Received %s, %s', response.headers, response.text)
    status = response.status_code
    if status == 200:
        tree = XML.fromstring(response.content)
        body = tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')[0]
        return body
    elif status == 500:
        tree = XML.fromstring(response.content)
        fault = tree.find('.//{http://schemas.xmlsoap.org/soap/envelope/}Fault'
            )
        if fault is None:
            response.raise_for_status()
        faultcode = fault.findtext('faultcode')
        faultstring = fault.findtext('faultstring')
        faultdetail = fault.find('detail')
        raise SoapFault(faultcode, faultstring, faultdetail)
    else:
        response.raise_for_status()
    return None