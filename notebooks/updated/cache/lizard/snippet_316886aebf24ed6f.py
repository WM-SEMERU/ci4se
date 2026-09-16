def _on_prop_changed(self, instance, meth_name, res, args, kwargs):
    if not self._itsme and meth_name == '__setitem__':
        self.update_widget(args[0])
    return