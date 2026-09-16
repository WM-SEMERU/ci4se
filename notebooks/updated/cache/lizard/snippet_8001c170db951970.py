def remove_declaration(self, decl):
    del self.declarations[self.declarations.index(decl)]
    decl.cache.reset()