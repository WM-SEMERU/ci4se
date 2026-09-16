def format_xml(xml_str: str, exceptions: bool=False):
    try:
        import xml.dom.minidom
        return xml.dom.minidom.parseString(xml_str).toprettyxml()
    except Exception:
        if exceptions:
            raise
        return xml_str