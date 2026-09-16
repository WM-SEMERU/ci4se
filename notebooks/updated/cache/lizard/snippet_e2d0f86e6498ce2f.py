def __create_file_name(self, message_no):
    cwd = os.getcwd()
    filename = '{0}_{1}.xml'.format(self.output_prefix, message_no)
    return os.path.join(cwd, filename)