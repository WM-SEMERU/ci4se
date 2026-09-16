def process(self, state, procedure=None, force_addr=None, **kwargs):
    addr = state.addr if force_addr is None else force_addr
    if procedure is None:
        if addr not in self.project._sim_procedures:
            if state.arch.name.startswith('ARM'
                ) and addr & 1 == 1 and addr - 1 in self.project._sim_procedures:
                procedure = self.project._sim_procedures[addr - 1]
            else:
                return SimSuccessors.failure()
        else:
            procedure = self.project._sim_procedures[addr]
    if isinstance(addr, SootAddressDescriptor):
        l.debug('Running %s (originally at %r)', repr(procedure), addr)
    else:
        l.debug('Running %s (originally at %#x)', repr(procedure), addr)
    return self.project.factory.procedure_engine.process(state, procedure,
        force_addr=force_addr, **kwargs)