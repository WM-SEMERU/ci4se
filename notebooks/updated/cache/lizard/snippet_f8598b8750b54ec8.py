def cmd(send, msg, args):
    if msg == 'list':
        fortunes = list_fortunes() + list_fortunes(True)
        send(' '.join(fortunes), ignore_length=True)
    else:
        output = get_fortune(msg, args['name'])
        for line in output.splitlines():
            send(line)