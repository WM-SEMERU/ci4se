def acts_as_state_machine(cls):
    assert not hasattr(cls, 'current_state'
        ), '{0} already has a "current_state" attribute!'.format(cls)
    assert not hasattr(cls, 'states'
        ), '{0} already has a "states" attribute!'.format(cls)

    def get_states(obj):
        return StateInfo.get_states(obj.__class__)

    def is_transition_failure_handler(obj):
        return all([any([inspect.ismethod(obj), inspect.isfunction(obj)]),
            getattr(obj, '___pystatemachine_is_transition_failure_handler',
            False)])
    transition_failure_handlers = sorted([value for name, value in inspect.
        getmembers(cls, is_transition_failure_handler)], key=lambda m:
        getattr(m,
        '___pystatemachine_transition_failure_handler_calling_sequence', 0))
    setattr(cls, '___pystatemachine_transition_failure_handlers',
        transition_failure_handlers)
    cls.current_state = property(fget=StateInfo.get_current_state)
    cls.states = property(fget=get_states)
    return cls