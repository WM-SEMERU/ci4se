def refresh_swagger(self):
    try:
        os.remove(self._get_swagger_filename(self.swagger_url))
    except EnvironmentError as e:
        logger.warn(os.strerror(e.errno))
    else:
        self.__init__()