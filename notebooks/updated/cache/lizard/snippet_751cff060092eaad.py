def copy_node(ret, element, msg):
    sub_element = etree.SubElement(ret, element.tag, attrib=element.attrib)
    ModelDiff.process_attrib(sub_element, msg)
    return sub_element