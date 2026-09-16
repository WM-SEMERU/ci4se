def getExim(exim_id):
    interfaces = filter(lambda i: i[0] == exim_id, get_instrument_interfaces())
    return interfaces and interfaces[0][1] or None