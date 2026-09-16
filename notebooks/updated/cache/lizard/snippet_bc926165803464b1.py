def add_ref(self, ref):
    self.refs[ref.insn_addr].append(ref)
    self.data_addr_to_ref[ref.memory_data.addr].append(ref)