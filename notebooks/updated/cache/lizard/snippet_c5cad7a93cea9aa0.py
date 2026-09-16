def strftime(self, dtime, format):
    format = self.STRFTIME_FORMATS.get(format + '_FORMAT', format)
    if six.PY2 and isinstance(format, six.text_type):
        format = format.encode('utf8')
    timestring = dtime.strftime(format)
    if six.PY2:
        timestring = timestring.decode('utf8')
    return timestring