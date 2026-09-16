def cmd(send, msg, args):
    if args['type'] == 'privmsg':
        send('Note-passing should be done in public.')
        return
    arguments = msg.split()
    if len(arguments) > 1:
        send(
            'Sorry, I can only perform the summoning ritual for one person at a time'
            )
        return
    elif len(arguments) == 0:
        send('Who shall I summon?')
        return
    nick = arguments[0]
    message = 'You have been summoned!'
    row = Notes(note=message, submitter='The Dark Gods', nick=nick, time=
        datetime.now())
    args['db'].add(row)
    send('%s has been summoned!' % nick)