def tag_reachable_scripts(cls, scratch):
    if getattr(scratch, 'hairball_prepared', False):
        return
    reachable = set()
    untriggered_events = {}
    for script in cls.iter_scripts(scratch):
        if not isinstance(script, kurt.Comment):
            starting_type = cls.script_start_type(script)
            if starting_type == cls.NO_HAT:
                script.reachable = False
            elif starting_type == cls.HAT_WHEN_I_RECEIVE:
                script.reachable = False
                message = script[0].args[0].lower()
                untriggered_events.setdefault(message, set()).add(script)
            else:
                script.reachable = True
                reachable.add(script)
    while reachable:
        for event in cls.get_broadcast_events(reachable.pop()):
            if event in untriggered_events:
                for script in untriggered_events.pop(event):
                    script.reachable = True
                    reachable.add(script)
    scratch.hairball_prepared = True