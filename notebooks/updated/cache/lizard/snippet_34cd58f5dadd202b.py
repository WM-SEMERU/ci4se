def postprocess(self):
    try:
        for name, item in self['addresses'][0].items():
            try:
                if name == 'indexInList':
                    continue
                self['addresses'][0][name] = unicode(self['addresses'][0][name]
                    )
                self['address'][name] = unicode(self['address'][name])
            except AttributeError:
                pass
    except (KeyError, IndexError):
        pass
    super(MambuClient, self).postprocess()