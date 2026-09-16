def validate(self):
    for header in self._requiredHeaders:
        if not self.headers.get(header, False):
            raise errors.ParseError('Missing Registration Header: ' + header)
    for notice in self.notifications:
        for header in self._requiredNotificationHeaders:
            if not notice.get(header, False):
                raise errors.ParseError('Missing Notification Header: ' +
                    header)