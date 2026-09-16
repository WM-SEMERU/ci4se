def parsePowerTable(uhfbandcap):
    bandtbl = {k: v for k, v in uhfbandcap.items() if k.startswith(
        'TransmitPowerLevelTableEntry')}
    tx_power_table = [0] * (len(bandtbl) + 1)
    for k, v in bandtbl.items():
        idx = v['Index']
        tx_power_table[idx] = int(v['TransmitPowerValue']) / 100.0
    return tx_power_table