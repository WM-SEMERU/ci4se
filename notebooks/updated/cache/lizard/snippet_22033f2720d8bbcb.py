def _read_from_cwlinput(in_file, work_dir, runtime, parallel, input_order,
    output_cwl_keys):
    with open(in_file) as in_handle:
        inputs = json.load(in_handle)
    items_by_key = {}
    input_files = []
    passed_keys = set([])
    for key, input_val in ((k, v) for k, v in inputs.items() if not k.
        startswith(('sentinel', 'ignore'))):
        if key.endswith('_toolinput'):
            key = key.replace('_toolinput', '')
        if input_order[key] == 'record':
            cur_keys, items = _read_cwl_record(input_val)
            passed_keys |= cur_keys
            items_by_key[key] = items
        else:
            items_by_key[tuple(key.split('__'))] = _cwlvar_to_wdl(input_val)
        input_files = _find_input_files(input_val, input_files)
    prepped = _merge_cwlinputs(items_by_key, input_order, parallel)
    out = []
    for data in prepped:
        if isinstance(data, (list, tuple)):
            out.append([_finalize_cwl_in(utils.to_single_data(x), work_dir,
                list(passed_keys), output_cwl_keys, runtime) for x in data])
        else:
            out.append(_finalize_cwl_in(data, work_dir, list(passed_keys),
                output_cwl_keys, runtime))
    return out, input_files