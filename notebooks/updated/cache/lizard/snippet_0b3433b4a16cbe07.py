def _beaglebone_id(self):
    try:
        with open('/sys/bus/nvmem/devices/0-00500/nvmem', 'rb') as eeprom:
            eeprom_bytes = eeprom.read(16)
    except FileNotFoundError:
        return None
    if eeprom_bytes[:4] != b'\xaaU3\xee':
        return None
    id_string = eeprom_bytes[4:].decode('ascii')
    for model, bb_ids in _BEAGLEBONE_BOARD_IDS.items():
        for bb_id in bb_ids:
            if id_string == bb_id[1]:
                return model
    return None