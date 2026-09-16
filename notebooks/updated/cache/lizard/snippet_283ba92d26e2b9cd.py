def filter(self, *args, **kwargs):
    ancestors = set()
    filtrates = set()
    config = type(self)(self.device, deepcopy(self.ele))
    results = config.xpath(*args, **kwargs)
    if isinstance(results, list):
        for node in results:
            if etree.iselement(node):
                ancestors |= set(list(node.iterancestors()))
                filtrates.add(node)
        if filtrates:
            config._node_filter(config.ele, ancestors, filtrates)
        else:
            config.ele = etree.Element(config_tag, nsmap={'nc': nc_url})
    return config