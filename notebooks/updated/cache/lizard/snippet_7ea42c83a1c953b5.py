def to_json(self, incl_uniqueid=False):
    lst = []
    for context in _contexts:
        lst += [v.to_json(incl_uniqueid=incl_uniqueid) for v in self.filter
            (context=context, check_visible=False, check_default=False).
            to_list()]
    return lst