def swo_read(self):
    try:
        return self._link.swo_read()
    except DAPAccess.Error as exc:
        six.raise_from(self._convert_exception(exc), exc)