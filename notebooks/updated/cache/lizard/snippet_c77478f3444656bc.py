def _get_bb_addr_from_instr(self, instr):
    current_method = self.state.addr.method
    try:
        bb = current_method.block_by_label[instr]
    except KeyError:
        l.error('Possible jump to a non-existing bb %s --> %d', self.state.
            addr, instr)
        raise IncorrectLocationException()
    return SootAddressDescriptor(current_method, bb.idx, 0)