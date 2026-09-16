def new(self, url, clone_from=None, bare=True):
    if clone_from:
        self.clone(path=url, bare=bare)
    elif url.startswith('http'):
        proxy = Proxy(url)
        proxy.new(path=url, bare=bare)
    else:
        local = Local.new(path=url, bare=bare)
    return Repo(url)