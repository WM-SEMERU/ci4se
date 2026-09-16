def handle_upnp_error(self, xml_error):
    xml_error = xml_error.encode('utf-8')
    error = XML.fromstring(xml_error)
    log.debug('Error %s', xml_error)
    error_code = error.findtext(
        './/{urn:schemas-upnp-org:control-1-0}errorCode')
    if error_code is not None:
        description = self.UPNP_ERRORS.get(int(error_code), '')
        raise SoCoUPnPException(message=
            'UPnP Error {} received: {} from {}'.format(error_code,
            description, self.soco.ip_address), error_code=error_code,
            error_description=description, error_xml=xml_error)
    else:
        log.error('Unknown error received from %s', self.soco.ip_address)
        raise UnknownSoCoException(xml_error)