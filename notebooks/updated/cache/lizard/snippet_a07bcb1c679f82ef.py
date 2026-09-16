def allocate(self, sim_size):
    size = self._conc_alloc_size(sim_size)
    addr = self.state.heap.heap_location
    self.state.heap.heap_location += size
    l.debug('Allocating %d bytes at address %#08x', size, addr)
    return addr