def replace(self, s, data, attrs=None):
    s = s.format(**self.rc['labels'])
    attrs = attrs or data.attrs
    if hasattr(getattr(data, 'psy', None), 'arr_name'):
        attrs = attrs.copy()
        attrs['arr_name'] = data.psy.arr_name
    s = safe_modulo(s, attrs)
    if isinstance(data, InteractiveList):
        data = data[0]
    tname = self.any_decoder.get_tname(next(self.plotter.
        iter_base_variables), data.coords)
    if tname is not None and tname in data.coords:
        time = data.coords[tname]
        if not time.values.ndim:
            try:
                s = pd.to_datetime(str(time.values[()])).strftime(s)
            except ValueError:
                pass
    if six.PY2:
        return s.decode('utf-8')
    return s