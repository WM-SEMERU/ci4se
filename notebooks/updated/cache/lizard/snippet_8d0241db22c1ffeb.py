def _getAppStoreResource(self, ctx, name):
    offer = self.frontPageItem.store.findFirst(offering.InstalledOffering, 
        offering.InstalledOffering.offeringName == unicode(name, 'ascii'))
    if offer is not None:
        pp = ixmantissa.IPublicPage(offer.application, None)
        if pp is not None:
            warn(
                'Use the sharing system to provide public pages, not IPublicPage'
                , category=DeprecationWarning, stacklevel=2)
            return pp.getResource()
        return SharingIndex(offer.application.open(), self.webViewer)
    return None