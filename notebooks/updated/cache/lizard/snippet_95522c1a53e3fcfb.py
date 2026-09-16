def attach_kernel_driver(self, interface):
    r
    self._ctx.managed_open()
    self._ctx.backend.attach_kernel_driver(self._ctx.handle, interface)