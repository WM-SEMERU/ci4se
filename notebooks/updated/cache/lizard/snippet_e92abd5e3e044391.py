def read_tree(input, schema):
    schema_to_function = {'dendropy': read_tree_dendropy, 'newick':
        read_tree_newick, 'nexml': read_tree_nexml, 'nexus': read_tree_nexus}
    if schema.lower() not in schema_to_function:
        raise ValueError('Invalid schema: %s (valid options: %s)' % (schema,
            ', '.join(sorted(schema_to_function.keys()))))
    return schema_to_function[schema.lower()](input)