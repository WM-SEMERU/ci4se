def autogen_argparse_block(extra_args=[]):
    grouped_args = []
    for argtup in __REGISTERED_ARGS__:
        argstr_list, type_, default, help_ = argtup
        argstr_set = set(argstr_list)
        found = False
        for index, (keyset, vals) in enumerate(grouped_args):
            if len(keyset.intersection(argstr_set)) > 0:
                keyset.update(argstr_set)
                vals.append(argtup)
                found = True
                break
        if not found:
            new_keyset = argstr_set
            new_vals = [argtup]
            grouped_args.append((new_keyset, new_vals))
    multi_groups = []
    for keyset, vals in grouped_args:
        if len(vals) > 1:
            multi_groups.append(vals)
    if len(multi_groups) > 0:
        import utool as ut
        print('Following arg was specified multiple times')
        print(ut.repr4(multi_groups, newlines=2))