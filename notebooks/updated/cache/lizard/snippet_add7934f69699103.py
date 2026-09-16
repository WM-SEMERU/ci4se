def ingress(self, envelope, http_headers, operation):
    if self._logger.isEnabledFor(logging.DEBUG):
        self._logger.debug(_RESPONSE_XML_LOG_LINE, etree.tostring(envelope,
            pretty_print=True))
    if self._logger.isEnabledFor(logging.WARN):
        warn_data = {}
        header = envelope.find(_HEADER_XPATH)
        fault = envelope.find(_FAULT_XPATH)
        if fault is not None:
            warn_data['faultMessage'] = fault.find('faultstring').text
            if header is not None:
                header_data = {re.sub(_REMOVE_NS_REGEXP, '', child.tag):
                    child.text for child in header[0]}
                warn_data.update(header_data)
            if 'serviceName' not in warn_data:
                warn_data['serviceName'
                    ] = operation.binding.wsdl.services.keys()[0]
            if 'methodName' not in warn_data:
                warn_data['methodName'] = operation.name
            self._logger.warn('Error summary: %s', warn_data)
    return envelope, http_headers