def convert_concat(net, node, module, builder):
    input_names, output_name = _get_input_output_name(net, node, 'all')
    name = node['name']
    mode = 'CONCAT'
    builder.add_elementwise(name=name, input_names=input_names, output_name
        =output_name, mode=mode)