def main(self, config_filename, file_names=None):
    self._io.title('Loader')
    if file_names:
        self.__load_list(config_filename, file_names)
    else:
        self.__load_all(config_filename)
    if self.error_file_names:
        self.__log_overview_errors()
        return 1
    else:
        return 0