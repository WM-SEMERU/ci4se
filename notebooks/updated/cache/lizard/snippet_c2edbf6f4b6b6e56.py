def _check_for_errors(self, response):
    if response.status_code != 200:
        xml_error = really_utf8(response.text)
        error_dom = XML.fromstring(xml_error)
        fault = error_dom.find('.//' + _ns_tag('s', 'Fault'))
        error_description = fault.find('faultstring').text
        error_code = EXCEPTION_STR_TO_CODE[error_description]
        message = 'UPnP Error {} received: {} from {}'.format(error_code,
            error_description, self._url)
        raise SoCoUPnPException(message=message, error_code=error_code,
            error_description=error_description, error_xml=really_utf8(
            response.text))