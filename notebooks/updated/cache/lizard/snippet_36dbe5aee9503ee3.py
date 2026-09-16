def init_generic_serial_dut(contextlist, conf, index, args):
    port = conf['serial_port']
    baudrate = args.baudrate if args.baudrate else conf.get('application', {}
        ).get('baudrate', 115200)
    serial_config = {}
    if args.serial_rtscts:
        serial_config['serial_rtscts'] = args.serial_rtscts
    elif args.serial_xonxoff:
        serial_config['serial_xonxoff'] = args.serial_xonxoff
    if args.serial_timeout:
        serial_config['serial_timeout'] = args.serial_timeout
    ch_mode_config = {}
    if args.serial_ch_size > 0:
        ch_mode_config['ch_mode'] = True
        ch_mode_config['ch_mode_chunk_size'] = args.serial_ch_size
    elif args.serial_ch_size is 0:
        ch_mode_config['ch_mode'] = False
    if args.ch_mode_ch_delay:
        ch_mode_config['ch_mode_ch_delay'] = args.ch_mode_ch_delay
    dut = DutSerial(name='D%d' % index, port=port, baudrate=baudrate,
        config=conf, ch_mode_config=ch_mode_config, serial_config=
        serial_config, params=args)
    dut.index = index
    dut.platform = conf.get('platform_name', 'serial')
    msg = 'Use device in serial port {} as D{}'
    contextlist.logger.info(msg.format(port, index))
    contextlist.duts.append(dut)
    contextlist.dutinformations.append(dut.get_info())