def new_object(cls, state, type_, symbolic=False, init_object=False):
    obj_ref = cls(heap_alloc_id=state.memory.get_new_uuid(), type_=type_,
        symbolic=symbolic)
    if init_object:
        l.info('>' * 15 + ' Initialize object %r ... ' + '>' * 15, obj_ref)
        init_method = resolve_method(state, '<init>', type_, init_class=False
            ).address()
        args = [SootArgument(obj_ref, obj_ref.type, is_this_ref=True)]
        init_state = state.project.simos.state_call(init_method, *args,
            base_state=state, ret_addr=SootAddressTerminator())
        simgr = state.project.factory.simgr(init_state)
        simgr.run()
        state.memory.vm_static_table = simgr.deadended[0
            ].memory.vm_static_table.copy()
        state.memory.heap = simgr.deadended[0].memory.heap.copy()
        l.debug('<' * 15 + ' Initialize object %r ... done ' + '<' * 15,
            obj_ref)
    return obj_ref