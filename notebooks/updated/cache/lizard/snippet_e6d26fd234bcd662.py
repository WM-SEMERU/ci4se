def add_url(self, *args, **kwargs):
    if len(args) == 1 and not kwargs and isinstance(args[0], UrlEntry):
        self.urls.append(args[0])
    else:
        self.urls.append(UrlEntry(*args, **kwargs))