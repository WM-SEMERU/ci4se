def get_attribute(file, element):
    try:
        root = ET.parse(file)
        element = root.find(element)
        return element.attrib
    except AttributeError:
        log.error('Unable to find element matching %s', element)
        return False