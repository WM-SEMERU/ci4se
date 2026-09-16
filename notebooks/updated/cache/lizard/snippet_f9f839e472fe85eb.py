def convert_transpose(net, node, module, builder):
    input_name, output_name = _get_input_output_name(net, node)
    name = node['name']
    param = _get_attrs(node)
    axes = literal_eval(param['axes'])
    builder.add_permute(name, axes, input_name, output_name)