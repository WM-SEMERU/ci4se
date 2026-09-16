def cmd(send, msg, args):
    parser = arguments.ArgParser(args['config'])
    parser.add_argument('--nick', action=arguments.NickParser)
    parser.add_argument('msg', nargs='*')
    try:
        cmdargs = parser.parse_args(msg)
    except arguments.ArgumentException as e:
        send(str(e))
        return
    if cmdargs.msg:
        if cmdargs.nick:
            send('--nick cannot be combined with a message')
        else:
            send(translate(' '.join(cmdargs.msg), False).strip())
    else:
        log = get_log(args['db'], cmdargs.nick, args['target'])
        if not log:
            send("Couldn't find a message from %s :(" % cmdargs.nick)
        else:
            send(translate(log))