def replace_aliases(cut_dict, aliases):
    for k, v in cut_dict.items():
        for k0, v0 in aliases.items():
            cut_dict[k] = cut_dict[k].replace(k0, '(%s)' % v0)