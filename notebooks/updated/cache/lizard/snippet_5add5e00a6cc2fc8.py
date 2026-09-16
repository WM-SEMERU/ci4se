def object_build_class(node, member, localname):
    basenames = [base.__name__ for base in member.__bases__]
    return _base_class_object_build(node, member, basenames, localname=
        localname)