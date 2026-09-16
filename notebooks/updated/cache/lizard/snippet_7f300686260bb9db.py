def _remove_unicode_encoding(xml_file):
    with salt.utils.files.fopen(xml_file, 'rb') as f:
        xml_content = f.read()
    modified_xml = re.sub(' encoding=[\\\'"]+unicode[\\\'"]+', '',
        xml_content.decode('utf-16'), count=1)
    xmltree = lxml.etree.parse(six.StringIO(modified_xml))
    return xmltree