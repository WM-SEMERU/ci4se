def get_saml_slos(cls, logout_request):
    try:
        root = etree.fromstring(logout_request)
        return root.xpath('//samlp:SessionIndex', namespaces={'samlp':
            'urn:oasis:names:tc:SAML:2.0:protocol'})
    except etree.XMLSyntaxError:
        return None