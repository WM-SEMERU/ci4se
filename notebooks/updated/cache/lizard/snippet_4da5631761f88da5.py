def auto_filters(cls):
    msg = (
        'Viewset must have auto_filters_fields or auto_filters_exclude attribute when using auto_filters decorator'
        )
    if not hasattr(cls, 'auto_filters_fields') and not hasattr(cls,
        'auto_filters_exclude'):
        raise AssertionError(msg)
    dict_ = {}
    view_model = get_view_model(cls)
    auto_filters_fields = get_auto_filters_fields(cls, view_model)
    for auto_filter in auto_filters_fields:
        dict_[auto_filter] = AutoFilters(name=auto_filter)
    dict_['Meta'] = type('Meta', (object,), {'model': view_model, 'fields': ()}
        )
    filter_class = type('DynamicFilterClass', (FilterSet,), dict_)
    cls.filter_class = filter_class
    return cls