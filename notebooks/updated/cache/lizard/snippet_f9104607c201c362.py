def getStore(self, name, domain):
    return IRealm(self.original.store.parent).accountByAddress(name, domain
        ).avatars.open()