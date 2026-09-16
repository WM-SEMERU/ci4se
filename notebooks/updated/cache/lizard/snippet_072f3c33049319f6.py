def combine_graph_defs(to_proto, from_proto):
    if from_proto.version != to_proto.version:
        raise ValueError('Cannot combine GraphDefs of different versions.')
    try:
        _safe_copy_proto_list_values(to_proto.node, from_proto.node, lambda
            n: n.name)
    except _ProtoListDuplicateKeyError as exc:
        raise ValueError('A GraphDef contains non-unique node names: %s' % exc)
    except _SameKeyDiffContentError as exc:
        raise ValueError(
            'Cannot combine GraphDefs because nodes share a name but contents are different: %s'
             % exc)
    try:
        _safe_copy_proto_list_values(to_proto.library.function, from_proto.
            library.function, lambda n: n.signature.name)
    except _ProtoListDuplicateKeyError as exc:
        raise ValueError(
            'A GraphDef contains non-unique function names: %s' % exc)
    except _SameKeyDiffContentError as exc:
        raise ValueError(
            'Cannot combine GraphDefs because functions share a name but are different: %s'
             % exc)
    try:
        _safe_copy_proto_list_values(to_proto.library.gradient, from_proto.
            library.gradient, lambda g: g.gradient_func)
    except _ProtoListDuplicateKeyError as exc:
        raise ValueError(
            'A GraphDef contains non-unique gradient function names: %s' % exc)
    except _SameKeyDiffContentError as exc:
        raise ValueError(
            'Cannot combine GraphDefs because gradients share a gradient_func name but map to different functions: %s'
             % exc)
    return to_proto