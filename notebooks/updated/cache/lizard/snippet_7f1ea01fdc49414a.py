def delete(self, context):
    status_code, msg = self.__endpoint.delete('/applications/application/{}'
        .format(self.__name))
    self.__available = False