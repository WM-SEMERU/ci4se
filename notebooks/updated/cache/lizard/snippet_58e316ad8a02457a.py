def is_valid(self, request_data, request_id=None, raise_exceptions=False):
    self.__error = None
    try:
        idp_data = self.__settings.get_idp_data()
        idp_entity_id = idp_data['entityId']
        get_data = request_data['get_data']
        if self.__settings.is_strict():
            res = OneLogin_Saml2_XML.validate_xml(self.document,
                'saml-schema-protocol-2.0.xsd', self.__settings.
                is_debug_active())
            if isinstance(res, str):
                raise OneLogin_Saml2_ValidationError(
                    'Invalid SAML Logout Request. Not match the saml-schema-protocol-2.0.xsd'
                    , OneLogin_Saml2_ValidationError.INVALID_XML_FORMAT)
            security = self.__settings.get_security_data()
            in_response_to = self.document.get('InResponseTo', None)
            if (request_id is not None and in_response_to and 
                in_response_to != request_id):
                raise OneLogin_Saml2_ValidationError(
                    'The InResponseTo of the Logout Response: %s, does not match the ID of the Logout request sent by the SP: %s'
                     % (in_response_to, request_id),
                    OneLogin_Saml2_ValidationError.WRONG_INRESPONSETO)
            issuer = self.get_issuer()
            if issuer is not None and issuer != idp_entity_id:
                raise OneLogin_Saml2_ValidationError(
                    'Invalid issuer in the Logout Response (expected %(idpEntityId)s, got %(issuer)s)'
                     % {'idpEntityId': idp_entity_id, 'issuer': issuer},
                    OneLogin_Saml2_ValidationError.WRONG_ISSUER)
            current_url = OneLogin_Saml2_Utils.get_self_url_no_query(
                request_data)
            destination = self.document.get('Destination', None)
            if destination and current_url not in destination:
                raise OneLogin_Saml2_ValidationError(
                    'The LogoutResponse was received at %s instead of %s' %
                    (current_url, destination),
                    OneLogin_Saml2_ValidationError.WRONG_DESTINATION)
            if security['wantMessagesSigned']:
                if 'Signature' not in get_data:
                    raise OneLogin_Saml2_ValidationError(
                        'The Message of the Logout Response is not signed and the SP require it'
                        , OneLogin_Saml2_ValidationError.NO_SIGNED_MESSAGE)
        return True
    except Exception as err:
        self.__error = str(err)
        debug = self.__settings.is_debug_active()
        if debug:
            print(err)
        if raise_exceptions:
            raise
        return False