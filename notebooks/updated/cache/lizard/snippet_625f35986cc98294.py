def dump_is_last(self, obj):
    if self._is_child(obj) and isinstance(obj, PIDNodeOrdered):
        if obj.children.count() > 0:
            return obj.children.ordered('asc').all()[-1] == self.context['pid']
        elif obj.draft_child:
            return obj.draft_child == self.context['pid']
        else:
            return True
    else:
        return None