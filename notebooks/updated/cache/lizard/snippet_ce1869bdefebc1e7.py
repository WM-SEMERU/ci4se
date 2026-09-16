def recv(self, picture, *args):
    return lib.zsock_recv(self._as_parameter_, picture, *args)