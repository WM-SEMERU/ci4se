def bind_permanent(type_to_bind: hexdi.core.restype, accessor: hexdi.core.
    clstype):
    hexdi.core.get_root_container().bind_type(type_to_bind, accessor,
        lifetime.PermanentLifeTimeManager)