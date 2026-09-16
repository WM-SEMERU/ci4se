def build_param_doc(arg_names, arg_types, arg_descs, remove_dup=True):
    param_keys = set()
    param_str = []
    for key, type_info, desc in zip(arg_names, arg_types, arg_descs):
        if key in param_keys and remove_dup:
            continue
        if key == 'num_args':
            continue
        param_keys.add(key)
        ret = '%s : %s' % (key, type_info)
        if len(desc) != 0:
            ret += '\n    ' + desc
        param_str.append(ret)
    doc_str = 'Parameters\n' + '----------\n' + '%s\n'
    doc_str = doc_str % '\n'.join(param_str)
    return doc_str