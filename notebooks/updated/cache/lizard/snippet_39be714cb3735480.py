def alias_resolving(self):
    alias_list = list(Alias.objects.all())
    for alias in self.make_request(resource='alias_resolving'):
        yield Alias._from_engine(alias, alias_list)