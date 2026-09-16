def edit_poll(args):
    if not args.isadmin:
        return 'Nope, not gonna do it.'
    msg = args.msg.split(maxsplit=1)
    if len(msg) < 2:
        return 'Syntax: !vote edit <pollnum> <question>'
    if not msg[0].isdigit():
        return 'Not A Valid Positive Integer.'
    pid = int(msg[0])
    poll = get_open_poll(args.session, pid)
    if poll is None:
        return 'That poll was deleted or does not exist!'
    poll.question = msg[1]
    return 'Poll updated!'