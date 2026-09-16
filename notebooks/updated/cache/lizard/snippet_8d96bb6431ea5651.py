def alias_action(self, *args, **kwargs):
    to = kwargs.pop('to', None)
    if not to:
        return
    error_message = (
        "You can't specify target ({}) as alias because it is real action name"
        .format(to))
    if to in list(itertools.chain(*self.aliased_actions.values())):
        raise Exception(error_message)
    self.aliased_actions.setdefault(to, []).extend(args)