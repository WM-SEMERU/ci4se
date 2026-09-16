def providerIsAuthoritative(providerID, canonicalID):
    lastbang = canonicalID.rindex('!')
    parent = canonicalID[:lastbang]
    return parent == providerID