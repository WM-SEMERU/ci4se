def _add_dunder_class(func, member):
    python_cls = member.__class__
    cls_name = getattr(python_cls, '__name__', None)
    if not cls_name:
        return
    cls_bases = [ancestor.__name__ for ancestor in python_cls.__bases__]
    ast_klass = build_class(cls_name, cls_bases, python_cls.__doc__)
    func.instance_attrs['__class__'] = [ast_klass]