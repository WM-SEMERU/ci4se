def get_value(self, name):
    code = "get_ipython().kernel.get_value('%s')" % name
    if self._reading:
        method = self.kernel_client.input
        code = '!' + code
    else:
        method = self.silent_execute
    wait_loop = QEventLoop()
    self.sig_got_reply.connect(wait_loop.quit)
    method(code)
    wait_loop.exec_()
    self.sig_got_reply.disconnect(wait_loop.quit)
    wait_loop = None
    if self._kernel_value is None:
        if self._kernel_reply:
            msg = self._kernel_reply[:]
            self._kernel_reply = None
            raise ValueError(msg)
    return self._kernel_value