def prune_unspecified_categories(modules, categories):
    res = {}
    for mod_name, mod_info in modules.items():
        mod_categories = mod_info.get('categories', all_categories)
        for category in categories:
            if category in mod_categories:
                break
        else:
            continue
        for input_name, input_info in mod_info['inputs'].items():
            for c in input_info['categories']:
                if c in categories:
                    break
            else:
                del mod_info['inputs'][input_name]
        for output_name, output_info in mod_info['outputs'].items():
            for c in output_info['categories']:
                if c in categories:
                    break
            else:
                del mod_info['outputs'][output_name]
        res[mod_name] = mod_info
    return res