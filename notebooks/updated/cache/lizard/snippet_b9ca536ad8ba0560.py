def client_setname(self, name):
    fut = self.execute(b'CLIENT', b'SETNAME', name)
    return wait_ok(fut)