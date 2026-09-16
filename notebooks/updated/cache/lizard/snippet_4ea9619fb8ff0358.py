def _write_rough_result_xml_to_file(self, xml, filename):
    error = xml.get('error', None)
    xml.set('error', 'incomplete')
    temp_filename = filename + '.tmp'
    with open(temp_filename, 'wb') as file:
        ET.ElementTree(xml).write(file, encoding='utf-8', xml_declaration=True)
    os.rename(temp_filename, filename)
    if error is not None:
        xml.set('error', error)
    else:
        del xml.attrib['error']