def cmd(send, msg, args):
    parser = arguments.ArgParser(args['config'])
    parser.add_argument('delay')
    parser.add_argument('msg', nargs='+')
    try:
        cmdargs = parser.parse_args(msg)
    except arguments.ArgumentException as e:
        send(str(e))
        return
    if isinstance(cmdargs.msg, list):
        cmdargs.msg = ' '.join(cmdargs.msg)
    cmdargs.delay = parse_time(cmdargs.delay)
    if cmdargs.delay is None:
        send('Invalid unit.')
    elif cmdargs.delay < 0:
        send('Time travel not yet implemented, sorry.')
    else:
        ident = args['handler'].workers.defer(cmdargs.delay, False, send,
            cmdargs.msg)
        send('Message deferred, ident: %s' % ident)