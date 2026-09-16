def add_abs_path_directories(opts_dict):
    assert_has_input_output(opts_dict)
    opts_dict['abs_input'] = path.abspath(opts_dict['input'])
    if opts_dict['is_dir']:
        opts_dict['abs_input'] += get_path_separator()
    opts_dict['abs_output'] = path.abspath(opts_dict['output']
        ) + get_path_separator()