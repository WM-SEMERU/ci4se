def _get_ruuvitag_datas(macs=[], search_duratio_sec=None, run_flag=RunFlag(
    ), bt_device=''):
    mac_blacklist = []
    start_time = time.time()
    data_iter = ble.get_datas(mac_blacklist, bt_device)
    for ble_data in data_iter:
        if search_duratio_sec and time.time(
            ) - start_time > search_duratio_sec:
            data_iter.send(StopIteration)
            break
        if not run_flag.running:
            data_iter.send(StopIteration)
            break
        if macs and not ble_data[0] in macs:
            continue
        data_format, data = RuuviTagSensor.convert_data(ble_data[1])
        if data is not None:
            state = get_decoder(data_format).decode_data(data)
            if state is not None:
                yield ble_data[0], state
        else:
            mac_blacklist.append(ble_data[0])