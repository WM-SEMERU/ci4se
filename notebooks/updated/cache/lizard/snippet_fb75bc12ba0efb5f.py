def logged_in(self):
    try:
        self._proxy.User.get({'ids': []})
        return True
    except Fault as e:
        if e.faultCode == 505 or e.faultCode == 32000:
            return False
        raise e