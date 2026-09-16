def build_configuration(self):
    configuration = config.Configuration()
    pegtree = pegnode.parse(self.filestring)
    for section_node in pegtree:
        if isinstance(section_node, pegnode.GlobalSection):
            configuration.globall = self.build_global(section_node)
        elif isinstance(section_node, pegnode.FrontendSection):
            configuration.frontends.append(self.build_frontend(section_node))
        elif isinstance(section_node, pegnode.DefaultsSection):
            configuration.defaults.append(self.build_defaults(section_node))
        elif isinstance(section_node, pegnode.ListenSection):
            configuration.listens.append(self.build_listen(section_node))
        elif isinstance(section_node, pegnode.UserlistSection):
            configuration.userlists.append(self.build_userlist(section_node))
        elif isinstance(section_node, pegnode.BackendSection):
            configuration.backends.append(self.build_backend(section_node))
    return configuration