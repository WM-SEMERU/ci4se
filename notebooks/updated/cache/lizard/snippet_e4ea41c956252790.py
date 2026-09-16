def subclass_of(*args):
    if len(args) == 2:
        typ, ref_type = args
        if not isinstance(ref_type, set):
            if issubclass(typ, ref_type):
                return True
            else:
                raise IsWrongType(wrong_value=typ, ref_type=ref_type)
        else:
            match = False
            for ref in ref_type:
                if issubclass(typ, ref):
                    match = True
                    break
            if match:
                return True
            else:
                raise IsWrongType(wrong_value=typ, ref_type=ref_type,
                    help_msg='Value should be a subclass of any of {ref_type}')
    elif len(args) == 1:
        ref_type = args[0]
        if not isinstance(ref_type, set):

            def subclass_of_ref(x):
                if issubclass(x, ref_type):
                    return True
                else:
                    raise IsWrongType(wrong_value=x, ref_type=ref_type)
        else:

            def subclass_of_ref(x):
                match = False
                for ref in ref_type:
                    if issubclass(x, ref):
                        match = True
                        break
                if match:
                    return True
                else:
                    raise IsWrongType(wrong_value=x, ref_type=ref_type,
                        help_msg=
                        'Value should be a subclass of any of {ref_type}')
        subclass_of_ref.__name__ = 'subclass_of_{}'.format(ref_type)
        return subclass_of_ref
    else:
        raise TypeError(
            'subclass_of expected 2 (normal) or 1 (function generator) arguments, got '
             + str(len(args)))