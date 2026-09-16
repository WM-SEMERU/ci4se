def gatherInput(**Config):
    r
    _type = Config.get('type')
    while True:
        try:
            got = raw_input('%s: ' % getLabel(Config))
        except EOFError:
            got = None
        if not got and 'default' in Config:
            return Config['default']
        try:
            return _type(got) if _type else got
        except ValueError as e:
            err(str(e) or '<invalid value>')
        except TypeError:
            err(str(e) or '<invalid value>')