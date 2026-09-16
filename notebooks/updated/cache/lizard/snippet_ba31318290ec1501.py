def indirect(self, interface):
    if interface == IWebViewer:
        return _AnonymousWebViewer(self.store)
    return super(AnonymousSite, self).indirect(interface)