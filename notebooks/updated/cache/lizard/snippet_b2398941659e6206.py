def process_signed_elements(self):
    sign_nodes = self.__query('//ds:Signature')
    signed_elements = []
    verified_seis = []
    verified_ids = []
    response_tag = '{%s}Response' % OneLogin_Saml2_Constants.NS_SAMLP
    assertion_tag = '{%s}Assertion' % OneLogin_Saml2_Constants.NS_SAML
    for sign_node in sign_nodes:
        signed_element = sign_node.getparent().tag
        if signed_element != response_tag and signed_element != assertion_tag:
            raise OneLogin_Saml2_ValidationError(
                'Invalid Signature Element %s SAML Response rejected' %
                signed_element, OneLogin_Saml2_ValidationError.
                WRONG_SIGNED_ELEMENT)
        if not sign_node.getparent().get('ID'):
            raise OneLogin_Saml2_ValidationError(
                'Signed Element must contain an ID. SAML Response rejected',
                OneLogin_Saml2_ValidationError.ID_NOT_FOUND_IN_SIGNED_ELEMENT)
        id_value = sign_node.getparent().get('ID')
        if id_value in verified_ids:
            raise OneLogin_Saml2_ValidationError(
                'Duplicated ID. SAML Response rejected',
                OneLogin_Saml2_ValidationError.DUPLICATED_ID_IN_SIGNED_ELEMENTS
                )
        verified_ids.append(id_value)
        ref = OneLogin_Saml2_XML.query(sign_node, './/ds:Reference')
        if ref:
            ref = ref[0]
            if ref.get('URI'):
                sei = ref.get('URI')[1:]
                if sei != id_value:
                    raise OneLogin_Saml2_ValidationError(
                        'Found an invalid Signed Element. SAML Response rejected'
                        , OneLogin_Saml2_ValidationError.INVALID_SIGNED_ELEMENT
                        )
                if sei in verified_seis:
                    raise OneLogin_Saml2_ValidationError(
                        'Duplicated Reference URI. SAML Response rejected',
                        OneLogin_Saml2_ValidationError.
                        DUPLICATED_REFERENCE_IN_SIGNED_ELEMENTS)
                verified_seis.append(sei)
        signed_elements.append(signed_element)
    if signed_elements:
        if not self.validate_signed_elements(signed_elements,
            raise_exceptions=True):
            raise OneLogin_Saml2_ValidationError(
                'Found an unexpected Signature Element. SAML Response rejected'
                , OneLogin_Saml2_ValidationError.UNEXPECTED_SIGNED_ELEMENTS)
    return signed_elements