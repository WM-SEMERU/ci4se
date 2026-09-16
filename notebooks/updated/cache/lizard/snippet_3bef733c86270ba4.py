def _closure_parent_pk(self):
    if hasattr(self, '%s_id' % self._closure_parent_attr):
        return getattr(self, '%s_id' % self._closure_parent_attr)
    else:
        parent = getattr(self, self._closure_parent_attr)
        return parent.pk if parent else None