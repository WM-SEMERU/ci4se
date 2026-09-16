def _get_url(self, obj):
    format_kwargs = {'app_label': obj._meta.app_label}
    try:
        format_kwargs['model_name'] = getattr(obj.__class__, 'get_url_name')()
    except AttributeError:
        format_kwargs['model_name'] = obj._meta.object_name.lower()
    return self._default_view_name % format_kwargs