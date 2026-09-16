def print_matching_trees(arg_dict, tree_format, exact, verbose):
    from peyotl.sugar import phylesystem_api
    tree_list = ot_find_tree(arg_dict, exact=exact, verbose=verbose)
    for tree_ref in tree_list:
        print(tree_ref)
        print(phylesystem_api.get(tree_ref, format=tree_format))