def url(self):
    if self.server_url is not None and self.recid is not None:
        return '/'.join([self.server_url, CFG_SITE_RECORD, str(self.recid)])
    else:
        return None