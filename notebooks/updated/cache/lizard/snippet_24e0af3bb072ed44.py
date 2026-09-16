def create_xml_file_from_string(self, content, destination=None):
    header_file = utils.create_temp_file_name(suffix='.h')
    try:
        with open(header_file, 'w+') as header:
            header.write(content)
        xml_file = self.create_xml_file(header_file, destination)
    finally:
        utils.remove_file_no_raise(header_file, self.__config)
    return xml_file