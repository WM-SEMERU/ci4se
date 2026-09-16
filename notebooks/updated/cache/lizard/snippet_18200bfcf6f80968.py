def get_variable_definitions(self, block_addr):
    if block_addr in self._outstates:
        return self._outstates[block_addr].variables
    return set()