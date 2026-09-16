def installProductOn(self, userstore):

    def install():
        i = Installation(store=userstore)
        i.types = self.types
        i.install()
    userstore.transact(install)