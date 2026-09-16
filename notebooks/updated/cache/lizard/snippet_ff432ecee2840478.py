def get_vgg(num_layers, pretrained=False, ctx=cpu(), root=os.path.join(base
    .data_dir(), 'models'), **kwargs):
    r
    layers, filters = vgg_spec[num_layers]
    net = VGG(layers, filters, **kwargs)
    if pretrained:
        from ..model_store import get_model_file
        batch_norm_suffix = '_bn' if kwargs.get('batch_norm') else ''
        net.load_parameters(get_model_file('vgg%d%s' % (num_layers,
            batch_norm_suffix), root=root), ctx=ctx)
    return net