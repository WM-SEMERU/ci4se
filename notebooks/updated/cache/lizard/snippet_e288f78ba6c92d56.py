def replace_greek(self, name):
    name = name.replace('gamma-delta', 'gammadelta')
    name = name.replace('interleukin-1 beta', 'interleukin-1beta')
    greek_present = False
    for greek_txt, uni in self.greek2uni.items():
        if greek_txt in name:
            greek_present = True
            name = name.replace(greek_txt, '{B}'.format(B=uni))
    if greek_present is True:
        name = unicode(name, 'utf-8')
    return name