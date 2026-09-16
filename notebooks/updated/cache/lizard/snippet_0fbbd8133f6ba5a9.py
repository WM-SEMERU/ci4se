def xresnet50_2(pretrained=False, **kwargs):
    model = XResNet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['xresnet50']))
    return model