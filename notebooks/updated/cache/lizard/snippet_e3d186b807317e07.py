def locate(self, path):
    return Zconfig(lib.zconfig_locate(self._as_parameter_, path), False)