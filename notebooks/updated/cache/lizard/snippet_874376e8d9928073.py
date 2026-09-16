def get_by_name(self, name, alias=None):
    search_filter = "[?name=='{}']".format(name)
    if alias:
        if self.version == 1:
            search_filter = (
                "accounts[?name=='{name}' || contains(alias, '{name}')]".
                format(name=name))
        elif self.version == 2:
            search_filter = ("[?name=='{name}' || contains(aliases, '{name}')]"
                .format(name=name))
    return self.get_all(search_filter)