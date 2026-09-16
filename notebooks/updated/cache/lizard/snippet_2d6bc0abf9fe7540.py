def find_available_vc_vers(self):
    ms = self.ri.microsoft
    vckeys = self.ri.vc, self.ri.vc_for_python, self.ri.vs
    vc_vers = []
    for hkey in self.ri.HKEYS:
        for key in vckeys:
            try:
                bkey = winreg.OpenKey(hkey, ms(key), 0, winreg.KEY_READ)
            except (OSError, IOError):
                continue
            subkeys, values, _ = winreg.QueryInfoKey(bkey)
            for i in range(values):
                try:
                    ver = float(winreg.EnumValue(bkey, i)[0])
                    if ver not in vc_vers:
                        vc_vers.append(ver)
                except ValueError:
                    pass
            for i in range(subkeys):
                try:
                    ver = float(winreg.EnumKey(bkey, i))
                    if ver not in vc_vers:
                        vc_vers.append(ver)
                except ValueError:
                    pass
    return sorted(vc_vers)