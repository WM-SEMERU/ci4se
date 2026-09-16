def default(self, obj):
    from ..model import Model
    from ..colors import Color
    from .has_props import HasProps
    if pd and isinstance(obj, (pd.Series, pd.Index)):
        return transform_series(obj, force_list=True)
    elif isinstance(obj, np.ndarray):
        return transform_array(obj, force_list=True)
    elif isinstance(obj, collections.deque):
        return list(map(self.default, obj))
    elif isinstance(obj, Model):
        return obj.ref
    elif isinstance(obj, HasProps):
        return obj.properties_with_values(include_defaults=False)
    elif isinstance(obj, Color):
        return obj.to_css()
    else:
        return self.transform_python_types(obj)