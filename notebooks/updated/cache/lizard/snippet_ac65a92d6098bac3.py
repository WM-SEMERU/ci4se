def _del_attrib(element):
    for tag in (operation_tag, insert_tag, value_tag, key_tag):
        if element.get(tag):
            del element.attrib[tag]
    return element