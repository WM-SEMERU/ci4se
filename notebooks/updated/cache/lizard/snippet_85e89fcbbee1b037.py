def get_datatable(self, **kwargs):
    if hasattr(self, '_datatable'):
        return self._datatable
    datatable_class = self.get_datatable_class()
    if datatable_class is None:


        class AutoMeta:
            model = self.model or self.get_queryset().model
        opts = AutoMeta()
        datatable_class = Datatable
    else:
        opts = datatable_class.options_class(datatable_class._meta)
    kwargs = self.get_datatable_kwargs(**kwargs)
    for meta_opt in opts.__dict__:
        if meta_opt in kwargs:
            setattr(opts, meta_opt, kwargs.pop(meta_opt))
    datatable_class = type('%s_Synthesized' % (datatable_class.__name__,),
        (datatable_class,), {'__module__': datatable_class.__module__,
        'Meta': opts})
    self._datatable = datatable_class(**kwargs)
    return self._datatable