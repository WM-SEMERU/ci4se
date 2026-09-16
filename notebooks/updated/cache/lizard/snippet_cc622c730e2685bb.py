def _decoder(self, obj):
    if '__class__' in obj:
        elem = eval(obj['__class__'])()
        elem.ident = obj['ident']
        elem.group = str(obj['group'])
        elem.name = str(obj['name'])
        elem.ctype = str(obj['ctype'])
        elem.pytype = str(obj['pytype'])
        elem.access = obj['access']
        return elem
    return obj