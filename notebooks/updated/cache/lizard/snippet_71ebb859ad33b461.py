def generate_request_xml(message_identifier_id, operation,
    lis_result_sourcedid, score):
    root = etree.Element('imsx_POXEnvelopeRequest', xmlns=
        'http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0')
    header = etree.SubElement(root, 'imsx_POXHeader')
    header_info = etree.SubElement(header, 'imsx_POXRequestHeaderInfo')
    version = etree.SubElement(header_info, 'imsx_version')
    version.text = 'V1.0'
    message_identifier = etree.SubElement(header_info, 'imsx_messageIdentifier'
        )
    message_identifier.text = message_identifier_id
    body = etree.SubElement(root, 'imsx_POXBody')
    xml_request = etree.SubElement(body, '%s%s' % (operation, 'Request'))
    record = etree.SubElement(xml_request, 'resultRecord')
    guid = etree.SubElement(record, 'sourcedGUID')
    sourcedid = etree.SubElement(guid, 'sourcedId')
    sourcedid.text = lis_result_sourcedid
    if score is not None:
        result = etree.SubElement(record, 'result')
        result_score = etree.SubElement(result, 'resultScore')
        language = etree.SubElement(result_score, 'language')
        language.text = 'en'
        text_string = etree.SubElement(result_score, 'textString')
        text_string.text = score.__str__()
    ret = "<?xml version='1.0' encoding='utf-8'?>\n{}".format(etree.
        tostring(root, encoding='utf-8').decode('utf-8'))
    log.debug('XML Response: \n%s', ret)
    return ret