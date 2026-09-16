def create_node(xml_node: XmlNode, **init_args):
    inst_type = get_inst_type(xml_node)
    init_args['xml_node'] = xml_node
    inst = create_inst(inst_type, **init_args)
    if not isinstance(inst, Node):
        inst = convert_to_node(inst, **init_args)
    return inst