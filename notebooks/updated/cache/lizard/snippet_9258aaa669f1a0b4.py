def vb_get_network_addresses(machine_name=None, machine=None,
    wait_for_pattern=None):
    if machine_name:
        machine = vb_get_box().findMachine(machine_name)
    ip_addresses = []
    log.debug('checking for power on:')
    if machine.state == _virtualboxManager.constants.MachineState_Running:
        log.debug('got power on:')
        if wait_for_pattern and not machine.getGuestPropertyValue(
            wait_for_pattern):
            log.debug('waiting for pattern:%s:', wait_for_pattern)
            return None
        _total_slots = machine.getGuestPropertyValue(
            '/VirtualBox/GuestInfo/Net/Count')
        if not _total_slots:
            log.debug('waiting for net count:%s:', wait_for_pattern)
            return None
        try:
            total_slots = int(_total_slots)
            for i in range(total_slots):
                try:
                    address = machine.getGuestPropertyValue(
                        '/VirtualBox/GuestInfo/Net/{0}/V4/IP'.format(i))
                    if address:
                        ip_addresses.append(address)
                except Exception as e:
                    log.debug(e.message)
        except ValueError as e:
            log.debug(e.message)
            return None
    log.debug('returning ip_addresses:%s:', ip_addresses)
    return ip_addresses