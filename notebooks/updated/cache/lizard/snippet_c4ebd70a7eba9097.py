def child_static(self, context):
    offeringTech = IOfferingTechnician(self.siteStore)
    installedOfferings = offeringTech.getInstalledOfferings()
    offeringsWithContent = dict([(offering.name, offering.staticContentPath
        ) for offering in installedOfferings.itervalues() if offering.
        staticContentPath])
    return StaticContent(offeringsWithContent, {})