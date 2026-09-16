def __proxy_password(self):
    passwd = copy(self._inp_proxy_password.value)
    self._inp_proxy_password.value = ''
    return passwd