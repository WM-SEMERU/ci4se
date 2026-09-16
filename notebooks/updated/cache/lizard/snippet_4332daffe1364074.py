def get_model(name, **kwargs):
    models = {'resnet18_v1': resnet18_v1, 'resnet34_v1': resnet34_v1,
        'resnet50_v1': resnet50_v1, 'resnet101_v1': resnet101_v1,
        'resnet152_v1': resnet152_v1, 'resnet18_v2': resnet18_v2,
        'resnet34_v2': resnet34_v2, 'resnet50_v2': resnet50_v2,
        'resnet101_v2': resnet101_v2, 'resnet152_v2': resnet152_v2, 'vgg11':
        vgg11, 'vgg13': vgg13, 'vgg16': vgg16, 'vgg19': vgg19, 'vgg11_bn':
        vgg11_bn, 'vgg13_bn': vgg13_bn, 'vgg16_bn': vgg16_bn, 'vgg19_bn':
        vgg19_bn, 'alexnet': alexnet, 'densenet121': densenet121,
        'densenet161': densenet161, 'densenet169': densenet169,
        'densenet201': densenet201, 'squeezenet1.0': squeezenet1_0,
        'squeezenet1.1': squeezenet1_1, 'inceptionv3': inception_v3,
        'mobilenet1.0': mobilenet1_0, 'mobilenet0.75': mobilenet0_75,
        'mobilenet0.5': mobilenet0_5, 'mobilenet0.25': mobilenet0_25,
        'mobilenetv2_1.0': mobilenet_v2_1_0, 'mobilenetv2_0.75':
        mobilenet_v2_0_75, 'mobilenetv2_0.5': mobilenet_v2_0_5,
        'mobilenetv2_0.25': mobilenet_v2_0_25}
    name = name.lower()
    if name not in models:
        raise ValueError(
            'Model %s is not supported. Available options are\n\t%s' % (
            name, '\n\t'.join(sorted(models.keys()))))
    return models[name](**kwargs)