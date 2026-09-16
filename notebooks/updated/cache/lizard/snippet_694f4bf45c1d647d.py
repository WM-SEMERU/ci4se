def create_description_node(field, state):
    doc_container_node = nodes.container()
    doc_container_node += parse_rst_content(field.doc, state)
    return doc_container_node