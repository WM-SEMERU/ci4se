def _set_up_context(cls):
    cls.context = AttributeDict()
    cls.context.new_meta = {}
    cls.context.new_transitions = {}
    cls.context.new_methods = {}