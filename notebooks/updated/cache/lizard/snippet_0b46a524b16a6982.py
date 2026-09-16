def keyserver(self):
    if 'PreferredKeyServer' in self._signature.subpackets:
        return next(iter(self._signature.subpackets['h_PreferredKeyServer'])
            ).uri
    return ''