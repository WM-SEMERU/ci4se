def update(self, update):
    params = shlex.split(update)
    if params[0] in self.addr:
        self.addr[params[0]].update(*params)
    else:
        a = Addr(self)
        self.addr[params[0]] = a
        self.addr[params[1]] = a
        a.update(*params)
        self.notify('addrmap_added', *[a], **{})