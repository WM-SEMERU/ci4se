def create_field_type_item_node(field, state):
    type_item = nodes.definition_list_item()
    type_item.append(nodes.term(text='Field type'))
    type_item_content = nodes.definition()
    type_item_content_p = nodes.paragraph()
    type_item_content_p += make_python_xref_nodes_for_type(type(field),
        state, hide_namespace=True)[0].children
    if field.optional:
        type_item_content_p += nodes.Text(' (optional)', ' (optional)')
    type_item_content += type_item_content_p
    type_item += type_item_content
    return type_item