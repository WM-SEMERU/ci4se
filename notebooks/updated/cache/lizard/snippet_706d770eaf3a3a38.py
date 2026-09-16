def run(self, name, *args):
    assert isinstance(name, string_types)
    name = self._aliases.get(name, name)
    action = self._actions_dict.get(name, None)
    if not action:
        raise ValueError("Action `{}` doesn't exist.".format(name))
    if not name.startswith('_'):
        logger.debug('Execute action `%s`.', name)
    return action.callback(*args)