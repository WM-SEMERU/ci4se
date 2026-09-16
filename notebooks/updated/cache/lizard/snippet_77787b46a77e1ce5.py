def init_class(self, class_, step_func=None):
    if self.is_class_initialized(class_):
        l.debug('Class %r already initialized.', class_)
        return
    l.debug('Initialize class %r.', class_)
    self.initialized_classes.add(class_)
    if not class_.is_loaded:
        l.warning('Class %r is not loaded in CLE. Skip initializiation.',
            class_)
        return
    clinit_method = resolve_method(self.state, '<clinit>', class_.name,
        include_superclasses=False, init_class=False)
    if clinit_method.is_loaded:
        javavm_simos = self.state.project.simos
        clinit_state = javavm_simos.state_call(addr=SootAddressDescriptor(
            clinit_method, 0, 0), base_state=self.state, ret_addr=
            SootAddressTerminator())
        simgr = self.state.project.factory.simgr(clinit_state)
        l.info('>' * 15 + ' Run class initializer %r ... ' + '>' * 15,
            clinit_method)
        simgr.run(step_func=step_func)
        l.debug('<' * 15 + ' Run class initializer %r ... done ' + '<' * 15,
            clinit_method)
        self.state.memory.vm_static_table = simgr.deadended[-1
            ].memory.vm_static_table.copy()
        self.state.memory.heap = simgr.deadended[-1].memory.heap.copy()
    else:
        l.debug(
            'Class initializer <clinit> is not loaded in CLE. Skip initializiation.'
            )