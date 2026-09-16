def _get_requested_spec(self, obj, spec_name):
    requested = self._specs_in[spec_name]
    if isinstance(requested, str):
        return _get_attr_by_tag(obj, requested, spec_name)
    else:
        return requested