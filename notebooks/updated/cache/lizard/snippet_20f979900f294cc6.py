def get_all_widget_classes():
    from leonardo.module.web.models import Widget
    _widgets = getattr(settings, 'WIDGETS', Widget.__subclasses__())
    widgets = []
    if isinstance(_widgets, dict):
        for group, widget_cls in six.iteritems(_widgets):
            widgets.extend(widget_cls)
    elif isinstance(_widgets, list):
        widgets = _widgets
    return load_widget_classes(widgets)