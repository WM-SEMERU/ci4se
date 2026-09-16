def _find_address_range(addresses):
    first = last = addresses[0]
    last_index = 0
    for ip in addresses[1:]:
        if ip._ip == last._ip + 1:
            last = ip
            last_index += 1
        else:
            break
    return first, last, last_index