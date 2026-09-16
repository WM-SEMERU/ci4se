def get_any_node(self, addr, is_syscall=None, anyaddr=False, force_fastpath
    =False):
    if not anyaddr:
        try:
            return self._nodes_by_addr[addr][0]
        except (KeyError, IndexError):
            pass
    if force_fastpath:
        return None
    for n in self.graph.nodes():
        if self.ident == 'CFGEmulated':
            cond = n.looping_times == 0
        else:
            cond = True
        if anyaddr and n.size is not None:
            cond = cond and n.addr <= addr < n.addr + n.size
        else:
            cond = cond and addr == n.addr
        if cond:
            if is_syscall is None:
                return n
            if n.is_syscall == is_syscall:
                return n
    return None