def document(self, wrapper):
    tag = wrapper[1].name
    ns = wrapper[1].namespace('ns0')
    return Element(tag, ns=ns)