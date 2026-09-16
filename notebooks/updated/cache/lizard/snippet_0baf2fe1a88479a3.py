def _load_from_native_memory(self, addr, data_type=None, data_size=None,
    no_of_elements=1, return_as_list=False):
    if addr is not None and self.state.solver.symbolic(addr):
        raise NotImplementedError('Symbolic addresses are not supported.')
    if not data_size:
        if data_type:
            data_size = ArchSoot.sizeof[data_type] // 8
        else:
            raise ValueError('Cannot determine the data size w/o a type.')
    native_memory_endness = self.state.arch.memory_endness
    values = []
    for i in range(no_of_elements):
        value = self.state.memory.load(addr + i * data_size, size=data_size,
            endness=native_memory_endness)
        if data_type:
            value = self.state.project.simos.cast_primitive(self.state,
                value=value, to_type=data_type)
        values.append(value)
    if no_of_elements == 1 and not return_as_list:
        return values[0]
    else:
        return values