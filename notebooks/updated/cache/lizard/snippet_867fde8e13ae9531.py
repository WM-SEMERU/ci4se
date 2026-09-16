def register_composer(self, type, composer, **meta):
    try:
        self.registered_formats[type]['composer'] = composer
    except KeyError:
        self.registered_formats[type] = {'composer': composer}
    if meta:
        self.register_meta(type, **meta)