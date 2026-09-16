def _make_it_list(dict_, field_name, value):
    prev_value = []
    if field_name in dict_:
        prev_value = dict_[field_name]
    if value is None:
        return prev_value
    elif isinstance(value, (tuple, list)):
        if field_name in ('source_port', 'destination_port'):
            portval = []
            for port in value:
                if not isinstance(port, (tuple, list)):
                    portval.append((port, port))
                else:
                    portval.append(port)
            translated_portval = []
            for port_start, port_end in portval:
                if not isinstance(port_start, int):
                    port_start = _translate_port(port_start)
                if not isinstance(port_end, int):
                    port_end = _translate_port(port_end)
                translated_portval.append((port_start, port_end))
            return list(set(prev_value + translated_portval))
        return list(set(prev_value + list(value)))
    if field_name in ('source_port', 'destination_port'):
        if not isinstance(value, int):
            value = _translate_port(value)
        return list(set(prev_value + [(value, value)]))
    return list(set(prev_value + [value]))