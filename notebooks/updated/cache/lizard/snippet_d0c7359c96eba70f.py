def verify(self):
    try:
        if self.timestamp_mismatch is not None:
            m = _iso8601_timestamp_regex.match(self.request_timestamp)
            year = int(m.group('year'))
            month = int(m.group('month'))
            day = int(m.group('day'))
            hour = int(m.group('hour'))
            minute = int(m.group('minute'))
            second = int(m.group('second'))
            req_ts = datetime(year, month, day, hour, minute, second)
            now = datetime.utcnow()
            if abs(req_ts - now) > timedelta(0, self.timestamp_mismatch):
                raise InvalidSignatureError('Timestamp mismatch')
        if self.expected_signature != self.request_signature:
            raise InvalidSignatureError(
                'Signature mismatch: expected %r, got %r' % (self.
                expected_signature, self.request_signature))
    except (AttributeError, KeyError, ValueError) as e:
        raise InvalidSignatureError(str(e))
    return True