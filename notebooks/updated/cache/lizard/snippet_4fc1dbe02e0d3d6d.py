def _wrapNavFrag(self, frag, useAthena):
    username = self._privateApplication._getUsername()
    cf = getattr(frag, 'customizeFor', None)
    if cf is not None:
        frag = cf(username)
    if useAthena:
        pageClass = GenericNavigationAthenaPage
    else:
        pageClass = GenericNavigationPage
    return pageClass(self._privateApplication, frag, self.
        _privateApplication.getPageComponents(), username)