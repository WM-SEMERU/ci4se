def convert_batchnorm(net, node, module, builder):
    input_name, output_name = _get_input_output_name(net, node)
    name = node['name']
    inputs = node['inputs']
    eps = 0.001
    use_global_stats = False
    fix_gamma = True
    attrs = _get_attrs(node)
    if 'eps' in attrs:
        eps = literal_eval(attrs['eps'])
    if 'fix_gamma' in attrs:
        fix_gamma = literal_eval(attrs['fix_gamma'])
    args, aux = module.get_params()
    gamma = args[_get_node_name(net, inputs[1][0])].asnumpy()
    beta = args[_get_node_name(net, inputs[2][0])].asnumpy()
    mean = aux[_get_node_name(net, inputs[3][0])].asnumpy()
    variance = aux[_get_node_name(net, inputs[4][0])].asnumpy()
    nb_channels = gamma.shape[0]
    if fix_gamma:
        gamma.fill(1.0)
    builder.add_batchnorm(name=name, channels=nb_channels, gamma=gamma,
        beta=beta, mean=mean, variance=variance, input_name=input_name,
        output_name=output_name, epsilon=eps)