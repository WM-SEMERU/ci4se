def mouse_area(self, handler, group=0, ident=None):
    key = ident or id(handler)
    if key not in self.mouse_proxies[group]:
        self.mouse_proxies[group][key] = MouseProxy(handler, ident)
    return self.mouse_proxies[group][key]