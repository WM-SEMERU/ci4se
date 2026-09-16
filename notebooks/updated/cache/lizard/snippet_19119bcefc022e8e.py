def address_line_1(self):
    formalised_address = self.formalised_address
    if formalised_address is None:
        return
    try:
        address = formalised_address.split(',')
    except Exception as e:
        if self._debug:
            logging.error('Error getting address_line_1. Error message: ' +
                e.args[0])
        return
    return address[0].strip()