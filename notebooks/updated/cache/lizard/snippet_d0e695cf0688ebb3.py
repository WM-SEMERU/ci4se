def train(self, *args, **kwargs):
    objs = self._do_transform(*args, **kwargs)
    obj_list = [objs] if not isinstance(objs, Iterable) else objs
    for obj in obj_list:
        if not isinstance(obj, ODPSModelExpr):
            continue
        for meta in ['predictor', 'recommender']:
            if meta not in self._metas:
                continue
            mod = __import__(self.__class__.__module__.__name__, fromlist=['']
                ) if not hasattr(self, '_env') else self._env
            action_cls_name = underline_to_capitalized(self._metas[meta])
            if not hasattr(mod, action_cls_name):
                action_cls_name = '_' + action_cls_name
            setattr(obj, '_' + meta, mod + '.' + action_cls_name)
    return objs