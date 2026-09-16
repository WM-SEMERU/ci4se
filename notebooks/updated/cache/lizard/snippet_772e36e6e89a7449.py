def generate_name_id(value, sp_nq, sp_format=None, cert=None, debug=False,
    nq=None):
    root = OneLogin_Saml2_XML.make_root('{%s}container' %
        OneLogin_Saml2_Constants.NS_SAML)
    name_id = OneLogin_Saml2_XML.make_child(root, '{%s}NameID' %
        OneLogin_Saml2_Constants.NS_SAML)
    if sp_nq is not None:
        name_id.set('SPNameQualifier', sp_nq)
    if sp_format is not None:
        name_id.set('Format', sp_format)
    if nq is not None:
        name_id.set('NameQualifier', nq)
    name_id.text = value
    if cert is not None:
        xmlsec.enable_debug_trace(debug)
        manager = xmlsec.KeysManager()
        manager.add_key(xmlsec.Key.from_memory(cert, xmlsec.KeyFormat.
            CERT_PEM, None))
        enc_data = xmlsec.template.encrypted_data_create(root, xmlsec.
            Transform.AES128, type=xmlsec.EncryptionType.ELEMENT, ns='xenc')
        xmlsec.template.encrypted_data_ensure_cipher_value(enc_data)
        key_info = xmlsec.template.encrypted_data_ensure_key_info(enc_data,
            ns='dsig')
        enc_key = xmlsec.template.add_encrypted_key(key_info, xmlsec.
            Transform.RSA_OAEP)
        xmlsec.template.encrypted_data_ensure_cipher_value(enc_key)
        enc_ctx = xmlsec.EncryptionContext(manager)
        enc_ctx.key = xmlsec.Key.generate(xmlsec.KeyData.AES, 128, xmlsec.
            KeyDataType.SESSION)
        enc_data = enc_ctx.encrypt_xml(enc_data, name_id)
        return '<saml:EncryptedID>' + compat.to_string(OneLogin_Saml2_XML.
            to_string(enc_data)) + '</saml:EncryptedID>'
    else:
        return OneLogin_Saml2_XML.extract_tag_text(root, 'saml:NameID')