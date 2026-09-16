def format_configfield_nodes(field_name, field, field_id, state, lineno):
    dtype_node = nodes.definition_list_item()
    dtype_node = nodes.term(text='Data type')
    dtype_def = nodes.definition()
    dtype_def_para = nodes.paragraph()
    name = '.'.join((field.dtype.__module__, field.dtype.__name__))
    dtype_def_para += pending_config_xref(rawsource=name)
    dtype_def += dtype_def_para
    dtype_node += dtype_def
    dl = nodes.definition_list()
    dl += dtype_node
    dl += create_field_type_item_node(field, state)
    desc_node = create_description_node(field, state)
    title = create_title_node(field_name, field, field_id, state, lineno)
    return [title, dl, desc_node]