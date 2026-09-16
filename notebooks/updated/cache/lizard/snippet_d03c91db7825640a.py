def output_tree_ensemble(tree_ensemble_obj, output_filename,
    attribute_names=None):
    for t, tree in enumerate(tree_ensemble_obj.estimators_):
        print('Writing Tree {0:d}'.format(t))
        out_file = open(output_filename + '.{0:d}.tree', 'w')
        tree_str = print_tree_recursive(tree.tree_, 0, attribute_names)
        out_file.write(tree_str)
        out_file.close()
    return