def parse_properties(node):
    d = dict()
    for child in node.findall('properties'):
        for subnode in child.findall('property'):
            cls = None
            try:
                if 'type' in subnode.keys():
                    module = importlib.import_module('builtins')
                    cls = getattr(module, subnode.get('type'))
            except AttributeError:
                logger.info(
                    'Type [} Not a built-in type. Defaulting to string-cast.')
            d[subnode.get('name')] = cls(subnode.get('value')
                ) if cls is not None else subnode.get('value')
    return d