def accessibles(self, roles=None):
    return [org['slug'] for org in self.get_accessibles(self.request, roles
        =roles)]