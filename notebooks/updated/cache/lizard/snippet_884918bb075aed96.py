def _parse_nicknameinuse(client, command, actor, args):
    nick, _, _ = args.rpartition(' ')
    client.dispatch_event('NICKNAMEINUSE', nick)