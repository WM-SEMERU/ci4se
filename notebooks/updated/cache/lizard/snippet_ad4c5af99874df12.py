def validate(self, lsid, check_existing=True):
    if not lsid.startswith(self.base_lsid):
        return False
    if check_existing and lsid in self.registered_modules:
        return False
    return True