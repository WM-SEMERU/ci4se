def _read_history(f, zone):
    pos, length = zone
    f.seek(pos, SEEK_SET)
    histories = []
    while f.tell() < pos + length:
        history = {'nSample': unpack(MAX_SAMPLE * 'I', f.read(MAX_SAMPLE * 
            4)), 'lines': unpack('H', f.read(2)), 'sectors': unpack('H', f.
            read(2)), 'base_time': unpack('H', f.read(2)), 'notch': unpack(
            'H', f.read(2)), 'colour': unpack(MAX_CAN_VIEW * 'B', f.read(
            MAX_CAN_VIEW)), 'selection': unpack(MAX_CAN_VIEW * 'B', f.read(
            MAX_CAN_VIEW)), 'description': f.read(64).strip(b'\x01\x00'),
            'inputsNonInv': unpack(MAX_CAN_VIEW * 'H', f.read(MAX_CAN_VIEW *
            2)), 'inputsInv': unpack(MAX_CAN_VIEW * 'H', f.read(
            MAX_CAN_VIEW * 2)), 'HiPass_Filter': unpack(MAX_CAN_VIEW * 'I',
            f.read(MAX_CAN_VIEW * 4)), 'LowPass_Filter': unpack(
            MAX_CAN_VIEW * 'I', f.read(MAX_CAN_VIEW * 4)), 'reference':
            unpack(MAX_CAN_VIEW * 'I', f.read(MAX_CAN_VIEW * 4)), 'free': f
            .read(1720).strip(b'\x01\x00')}
        histories.append(history)
    return histories