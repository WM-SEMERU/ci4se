def isNewerThan(self, other):
    if self.getValue('name') == other.getValue('name'):
        if other.getValue('version'):
            if not other.getValue('version'):
                return False
            else:
                return LooseVersion(self.getValue('version')) > LooseVersion(
                    other.getValue('version'))
        else:
            return True
    else:
        return False