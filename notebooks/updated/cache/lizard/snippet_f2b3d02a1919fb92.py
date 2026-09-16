def format_dictfield_nodes(field_name, field, field_id, state, lineno):
    valuetype_item = nodes.definition_list_item()
    valuetype_item = nodes.term(text='Value type')
    valuetype_def = nodes.definition()
    valuetype_def += make_python_xref_nodes_for_type(field.itemtype, state,
        hide_namespace=False)
    valuetype_item += valuetype_def
    dl = nodes.definition_list()
    dl += create_default_item_node(field, state)
    dl += create_field_type_item_node(field, state)
    dl += create_keytype_item_node(field, state)
    dl += valuetype_item
    desc_node = create_description_node(field, state)
    title = create_title_node(field_name, field, field_id, state, lineno)
    return [title, dl, desc_node]