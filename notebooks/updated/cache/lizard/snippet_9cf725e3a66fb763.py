def _execute_simple_query(self, query):
    self._logger.info('Execute simple query: [{}]'.format(query))
    self.connection.write(messages.Query(query))
    self._message = self.connection.read_message()
    if isinstance(self._message, messages.ErrorResponse):
        raise errors.QueryError.from_error_response(self._message, query)
    elif isinstance(self._message, messages.RowDescription):
        self.description = [Column(fd, self.unicode_error) for fd in self.
            _message.fields]
        self._message = self.connection.read_message()
        if isinstance(self._message, messages.ErrorResponse):
            raise errors.QueryError.from_error_response(self._message, query)