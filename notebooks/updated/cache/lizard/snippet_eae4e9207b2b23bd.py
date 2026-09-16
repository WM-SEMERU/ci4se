def get_port_vendor_info(port=None):
    port_info_dict = dict((x[0], x[2]) for x in serial.tools.list_ports.
        comports())
    return port_info_dict[port] if port is not None else port_info_dict