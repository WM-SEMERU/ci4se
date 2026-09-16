def cmd(send, _, args):

    def lenny_send(msg):
        send(gen_lenny(msg))
    key = args['config']['api']['bitlykey']
    cmds = [lambda : gen_fortune(lenny_send), lambda : gen_urban(lenny_send,
        args['db'], key)]
    choice(cmds)()