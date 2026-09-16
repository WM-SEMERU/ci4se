def addIdentifier(self, identifier=None, seed=None, signer=None, alias=None,
    didMethodName=None):
    dm = self.didMethods.get(didMethodName)
    signer = signer or dm.newSigner(identifier=identifier, seed=seed)
    self.idsToSigners[signer.identifier] = signer
    if self.defaultId is None:
        self.defaultId = signer.identifier
    if alias:
        signer.alias = alias
    if signer.alias:
        self.aliasesToIds[signer.alias] = signer.identifier
    return signer.identifier, signer