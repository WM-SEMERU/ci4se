def build_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('sensor_graph', type=str, help=
        'The sensor graph file to load and run.')
    parser.add_argument('--stop', '-s', action='append', default=[], type=
        str, help='A stop condition for when the simulation should end.')
    parser.add_argument('--realtime', '-r', action='store_true', help=
        'Do not accelerate the simulation, pin the ticks to wall clock time')
    parser.add_argument('--watch', '-w', action='append', default=[], help=
        'A stream to watch and print whenever writes are made.')
    parser.add_argument('--trace', '-t', help=
        'Trace all writes to output streams to a file')
    parser.add_argument('--disable-optimizer', action='store_true', help=
        'disable the sensor graph optimizer completely')
    parser.add_argument('--mock-rpc', '-m', action='append', type=str,
        default=[], help=
        'mock an rpc, format should be <slot id>:<rpc_id> = value.  For example -m "slot 1:0x500a = 10"'
        )
    parser.add_argument('--port', '-p', help=
        'The port to use to connect to a device if we are semihosting')
    parser.add_argument('--semihost-device', '-d', type=lambda x: int(x, 0),
        help=
        'The device id of the device we should semihost this sensor graph on.')
    parser.add_argument('-c', '--connected', action='store_true', help=
        'Simulate with a user connected to the device (to enable realtime outputs)'
        )
    parser.add_argument('-i', '--stimulus', action='append', default=[],
        help=
        'Push a value to an input stream at the specified time (or before starting).  The syntax is [time: ][system ]input X = Y where X and Y are integers'
        )
    return parser