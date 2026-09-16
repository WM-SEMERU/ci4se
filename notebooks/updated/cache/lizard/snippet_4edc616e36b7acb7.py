def _add_data_reference(self, irsb_addr, stmt_idx, insn_addr, data_addr,
    data_size=None, data_type=None):
    if not self.project.loader.find_segment_containing(data_addr):
        for segment in self.project.loader.main_object.segments:
            if segment.vaddr + segment.memsize == data_addr:
                new_data = False
                if data_addr not in self._memory_data:
                    data = MemoryData(data_addr, 0, MemoryDataSort.
                        SegmentBoundary)
                    self._memory_data[data_addr] = data
                    new_data = True
                if new_data or self._extra_cross_references:
                    cr = CodeReference(insn_addr, irsb_addr, stmt_idx,
                        memory_data=self.model.memory_data[data_addr])
                    self.model.references.add_ref(cr)
                break
        return
    new_data = False
    if data_addr not in self._memory_data:
        if data_type is not None and data_size is not None:
            data = MemoryData(data_addr, data_size, data_type, max_size=
                data_size)
        else:
            data = MemoryData(data_addr, 0, MemoryDataSort.Unknown)
        self._memory_data[data_addr] = data
        new_data = True
    if new_data or self._extra_cross_references:
        cr = CodeReference(insn_addr, irsb_addr, stmt_idx, memory_data=self
            .model.memory_data[data_addr])
        self.model.references.add_ref(cr)
    self.insn_addr_to_memory_data[insn_addr] = self._memory_data[data_addr]