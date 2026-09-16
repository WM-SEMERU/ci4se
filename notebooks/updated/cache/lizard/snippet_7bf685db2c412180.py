def read_string(self, content):
    header_file = utils.create_temp_file_name(suffix='.h')
    with open(header_file, 'w+') as f:
        f.write(content)
    try:
        decls = self.read_file(header_file)
    except Exception:
        utils.remove_file_no_raise(header_file, self.__config)
        raise
    utils.remove_file_no_raise(header_file, self.__config)
    return decls