def merged_args_dicts(global_args, subcommand_args):
    merged = global_args.copy()
    for key, val in subcommand_args.items():
        if key not in merged:
            merged[key] = val
        elif type(merged[key]) is type(val) is bool:
            merged[key] = merged[key] or val
        else:
            raise RuntimeError('Unmergable args.')
    return merged