def find_class(self, cls):
    for doc_cls in self.classes():
        if cls is doc_cls.cls:
            return doc_cls
    for module in self.submodules():
        doc_cls = module.find_class(cls)
        if not isinstance(doc_cls, External):
            return doc_cls
    return External('%s.%s' % (cls.__module__, cls.__name__))