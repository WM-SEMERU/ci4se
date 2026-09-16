def dumps(map, root_name, root_attributes=None):
    xml = ''
    try:
        implementation = getDOMImplementation()
    except ImportError as i:
        raise XMLErrorUtils(i, 'Erro ao obter o DOMImplementation')
    doc = implementation.createDocument(None, root_name, None)
    try:
        root = doc.documentElement
        if root_attributes is not None:
            for key, value in root_attributes.iteritems():
                attribute = doc.createAttribute(key)
                attribute.nodeValue = value
                root.setAttributeNode(attribute)
        _add_nodes_to_parent(map, root, doc)
        xml = doc.toxml('UTF-8')
    except InvalidCharacterErr as i:
        raise InvalidNodeNameXMLError(i, 
            'Valor inválido para nome de uma TAG de XML: %s' % root_name)
    finally:
        doc.unlink()
    return xml