def _mainType(self, resp):
    if self.PY2:
        return resp.headers.maintype
    elif self.PY3:
        return resp.headers.get_content_maintype()
    else:
        return None