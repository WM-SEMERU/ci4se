def _get_url(self, filename):
    return self.cdn_url.format(self.mver, self.relnum, filename)