def set_lastmodified_date(self, date=None):
    if date:
        match = re.match(DATE_REGEX, date)
        if not match:
            raise IOCParseError(
                'last-modified date is not valid.  Must be in the form YYYY-MM-DDTHH:MM:SS'
                )
    ioc_et.set_root_lastmodified(self.root, date)
    return True