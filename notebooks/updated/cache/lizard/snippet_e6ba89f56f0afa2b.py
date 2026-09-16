def ac_factory(path=''):
    acs = []
    if path:
        if path not in sys.path:
            sys.path.insert(0, path)
        for fil in os.listdir(path):
            if fil.endswith('.py'):
                mod = import_module(fil[:-3])
                for key, item in mod.__dict__.items():
                    if key.startswith('__'):
                        continue
                    if isinstance(item, dict
                        ) and 'to' in item and 'fro' in item:
                        atco = AttributeConverter(item['identifier'])
                        atco.from_dict(item)
                        acs.append(atco)
    else:
        from saml2 import attributemaps
        for typ in attributemaps.__all__:
            mod = import_module('.%s' % typ, 'saml2.attributemaps')
            for key, item in mod.__dict__.items():
                if key.startswith('__'):
                    continue
                if isinstance(item, dict) and 'to' in item and 'fro' in item:
                    atco = AttributeConverter(item['identifier'])
                    atco.from_dict(item)
                    acs.append(atco)
    return acs