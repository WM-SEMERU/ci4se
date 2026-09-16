def hide(self):
    self.visible = False
    if self.proxy_is_active:
        self.proxy.ensure_hidden()