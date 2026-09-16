def absolute_url(self):
    if self.is_root():
        return utils.concat_urls(self.url)
    return utils.concat_urls(self.parent.absolute_url, self.url)