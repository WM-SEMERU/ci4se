def get_title(self):
    if self.title is None:
        url = ''
        if self.base_url:
            url = self.base_url
        elif self.url:
            url = self.url
        self.title = url
        if '/' in url:
            title = url.rsplit('/', 1)[1]
            if title:
                self.title = title
    return self.title