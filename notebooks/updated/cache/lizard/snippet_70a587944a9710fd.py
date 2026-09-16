def run_from_command_line():
    for commands_conf in firenado.conf.management['commands']:
        logger.debug('Loading %s commands from %s.' % (commands_conf['name'
            ], commands_conf['module']))
        exec('import %s' % commands_conf['module'])
    command_index = 1
    for arg in sys.argv[1:]:
        command_index += 1
        if arg[0] != '-':
            break
    parser = FirenadoArgumentParser(prog=os.path.split(sys.argv[0])[1],
        add_help=False)
    parser.add_argument('-h', '--help', default=argparse.SUPPRESS)
    parser.add_argument('command', default='help', help='Command to executed')
    try:
        namespace = parser.parse_args(sys.argv[1:command_index])
        if not command_exists(namespace.command):
            show_command_line_usage(parser)
        else:
            run_command(namespace.command, sys.argv[command_index - 1:])
    except FirenadoArgumentError:
        show_command_line_usage(parser, True)