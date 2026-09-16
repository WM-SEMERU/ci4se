def set_serializer(self, serializer_name, compression=None):
    self.serializer = Serializer(serializer_name, charset='UTF-8',
        compression=compression)
    self.logger.debug('using serializer: ' + serializer_name)