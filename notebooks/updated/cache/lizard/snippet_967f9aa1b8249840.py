def run_device_command(sp):
    parser = sp.add_parser('run-device', help=
        'run an oct device for multi-HQ tests')
    parser.add_argument('device', help='The project directory', choices=[
        'forwarder', 'streamer'])
    parser.add_argument('-f', '--frontend', help='frontend port', type=int,
        required=True)
    parser.add_argument('-b', '--backend', help='backend port', type=int,
        required=True)
    parser.set_defaults(func=run_device)