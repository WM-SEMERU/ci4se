def _handle_actiongeturl(self, _):
    obj = _make_object('ActionGetURL')
    obj.UrlString = self._get_struct_string()
    obj.TargetString = self._get_struct_string()
    yield obj