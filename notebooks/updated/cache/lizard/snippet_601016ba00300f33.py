def getJSMinimumVolume(self, **kw):
    default = self.Schema()['MinimumVolume'].get(self)
    try:
        mgdefault = default.split(' ', 1)
        mgdefault = mg(float(mgdefault[0]), mgdefault[1])
    except:
        mgdefault = mg(0, 'ml')
    try:
        return str(mgdefault.ounit('ml'))
    except:
        pass
    try:
        return str(mgdefault.ounit('g'))
    except:
        pass
    return str(default)