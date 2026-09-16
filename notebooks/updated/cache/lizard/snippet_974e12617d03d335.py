def recursive_sort(data_structure):
    if not isinstance(data_structure, _primitive_types):
        is_meta = isinstance(data_structure, Meta)
        was_dict = isinstance(data_structure, WasDict)
        if not (is_meta or was_dict):
            was_dict = isinstance(data_structure, dict)
            if not was_dict:
                try:
                    data_structure = data_structure.__dict__
                    was_dict = True
                except:
                    pass
            try:
                data_structure = data_structure.items()
            except:
                pass
        tlen = -1
        try:
            tlen = len(data_structure)
        except:
            pass
        if tlen != -1:
            try:
                if was_dict:
                    return tuple(sorted([(recursive_sort(x[0]),
                        recursive_sort(x[1])) for x in data_structure], key
                        =TraversalBasedReprCompare))
                elif is_meta:
                    return data_structure[0:-1] + [recursive_sort(
                        data_structure[-1])]
                else:
                    return tuple(sorted([recursive_sort(x) for x in
                        data_structure], key=TraversalBasedReprCompare))
            except:
                pass
    return data_structure