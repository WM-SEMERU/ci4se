def read_holding_registers(slave_id, starting_address, quantity):
    function = ReadHoldingRegisters()
    function.starting_address = starting_address
    function.quantity = quantity
    return _create_request_adu(slave_id, function.request_pdu)