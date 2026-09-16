def _set_complete_option(cls):
    get_config = cls.context.get_config
    complete = get_config('complete', None)
    if complete is None:
        conditions = [get_config('transitions', False), get_config(
            'named_transitions', False)]
        complete = not any(conditions)
    cls.context.new_meta['complete'] = complete