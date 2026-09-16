def create_key_info_node(security_token):
    key_info = etree.Element(ns_id('KeyInfo', ns.dsns))
    sec_token_ref = etree.SubElement(key_info, ns_id(
        'SecurityTokenReference', ns.wssens))
    sec_token_ref.set(ns_id('TokenType', ns.wssens), security_token.get(
        'ValueType'))
    reference = etree.SubElement(sec_token_ref, ns_id('Reference', ns.wssens))
    reference.set('ValueType', security_token.get('ValueType'))
    reference.set('URI', '#%s' % security_token.get(WSU_ID))
    return key_info