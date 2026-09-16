def _detect_available_configs():
    if ics is None:
        return []
    try:
        devices = ics.find_devices()
    except Exception as e:
        logger.debug('Failed to detect configs: %s', e)
        return []
    return [{'interface': 'neovi', 'serial': NeoViBus.get_serial_number(
        device)} for device in devices]