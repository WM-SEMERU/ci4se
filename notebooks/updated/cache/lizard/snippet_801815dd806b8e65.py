def _preprocess_typecheck(argSig, argspecs, slf_or_clsm=False):
    vargs = argspecs.varargs
    try:
        kw = argspecs.keywords
    except AttributeError:
        kw = argspecs.varkw
    try:
        kwonly = argspecs.kwonlyargs
    except AttributeError:
        kwonly = None
    if not vargs is None or not kw is None:
        arg_type_lst = list(get_Tuple_params(argSig))
        if not vargs is None:
            vargs_pos = len(argspecs.args) - 1 if slf_or_clsm else len(argspecs
                .args)
            try:
                vargs_type = typing.Sequence[arg_type_lst[vargs_pos]]
            except IndexError:
                vargs_type = typing.Sequence[typing.Any]
            try:
                arg_type_lst[vargs_pos] = vargs_type
            except IndexError:
                arg_type_lst.append(vargs_type)
        if not kw is None:
            kw_pos = len(argspecs.args)
            if slf_or_clsm:
                kw_pos -= 1
            if not vargs is None:
                kw_pos += 1
            if not kwonly is None:
                kw_pos += len(kwonly)
            try:
                kw_type = typing.Dict[str, arg_type_lst[kw_pos]]
            except IndexError:
                kw_type = typing.Dict[str, typing.Any]
            try:
                arg_type_lst[kw_pos] = kw_type
            except IndexError:
                arg_type_lst.append(kw_type)
        return typing.Tuple[tuple(arg_type_lst)]
    else:
        return argSig