def _structure_dict(self, obj, cl):
    if is_bare(cl) or cl.__args__ == (Any, Any):
        return dict(obj)
    else:
        key_type, val_type = cl.__args__
        if key_type is Any:
            val_conv = self._structure_func.dispatch(val_type)
            return {k: val_conv(v, val_type) for k, v in obj.items()}
        elif val_type is Any:
            key_conv = self._structure_func.dispatch(key_type)
            return {key_conv(k, key_type): v for k, v in obj.items()}
        else:
            key_conv = self._structure_func.dispatch(key_type)
            val_conv = self._structure_func.dispatch(val_type)
            return {key_conv(k, key_type): val_conv(v, val_type) for k, v in
                obj.items()}