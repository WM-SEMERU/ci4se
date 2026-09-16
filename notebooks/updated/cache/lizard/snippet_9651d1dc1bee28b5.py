def add_namespace(self, name, a_namespace):
    self.namespaces[name] = a_namespace
    for k in a_namespace.keys_breadth_first():
        an_option = a_namespace[k]
        if not an_option.foreign_data:
            an_option.foreign_data = DotDict()
        an_option.foreign_data['argparse.owning_subparser_name'] = name