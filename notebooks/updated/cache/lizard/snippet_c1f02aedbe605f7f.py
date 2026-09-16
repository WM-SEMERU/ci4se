def process_xml(xml_str):
    try:
        tree = ET.XML(xml_str, parser=UTB())
    except ET.ParseError as e:
        logger.error('Could not parse XML string')
        logger.error(e)
        return None
    sp = _process_elementtree(tree)
    return sp