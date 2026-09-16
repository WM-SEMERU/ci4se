def add_data(self, addr, data):
    if len(data) == 0:
        return
    if not self.flash.region.contains_range(start=addr, length=len(data)):
        raise FlashFailure(
            "Flash address range 0x%x-0x%x is not contained within region '%s'"
             % (addr, addr + len(data) - 1, self.flash.region.name))
    self.flash_operation_list.append(_FlashOperation(addr, data))
    self.buffered_data_size += len(data)
    self.flash_operation_list = sorted(self.flash_operation_list, key=lambda
        operation: operation.addr)
    prev_flash_operation = None
    for operation in self.flash_operation_list:
        if prev_flash_operation is not None:
            if prev_flash_operation.addr + len(prev_flash_operation.data
                ) > operation.addr:
                raise ValueError(
                    'Error adding data - Data at 0x%x..0x%x overlaps with 0x%x..0x%x'
                     % (prev_flash_operation.addr, prev_flash_operation.
                    addr + len(prev_flash_operation.data), operation.addr, 
                    operation.addr + len(operation.data)))
        prev_flash_operation = operation