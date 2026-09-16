def exception(self):
    buf = traceback.format_exception_only(self.exc_type, self.exc_value)
    rv = ''.join(buf).strip()
    return to_unicode(rv, 'utf-8', 'replace')