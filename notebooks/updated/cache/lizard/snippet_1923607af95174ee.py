def parse_logout_request(self, message_text):
    result = {}
    xml_document = parseString(message_text)
    for node in xml_document.getElementsByTagName('saml:NameId'):
        for child in node.childNodes:
            if child.nodeType == child.TEXT_NODE:
                result['name_id'] = child.nodeValue.strip()
    for node in xml_document.getElementsByTagName('samlp:SessionIndex'):
        for child in node.childNodes:
            if child.nodeType == child.TEXT_NODE:
                result['session_index'] = str(child.nodeValue.strip())
    for key in xml_document.documentElement.attributes.keys():
        result[str(key)] = str(xml_document.documentElement.getAttribute(key))
    logging.debug('[CAS] LogoutRequest:\n{}'.format(json.dumps(result,
        sort_keys=True, indent=4, separators=[',', ': '])))
    return result