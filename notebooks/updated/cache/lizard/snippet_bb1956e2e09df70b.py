def check_zip(self, token):
    if self.zip is None:
        if self.last_matched is not None:
            return False
        if len(token) == 5 and re.match('\\d{5}', token):
            self.zip = self._clean(token)
            return True
    return False