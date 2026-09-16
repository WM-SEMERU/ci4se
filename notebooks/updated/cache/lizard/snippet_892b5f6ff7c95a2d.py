def do_mute(self, sender, body, args):
    if sender.get('MUTED'):
        self.send_message('you are already muted', sender)
    else:
        self.broadcast('%s has muted this chatroom' % (sender['NICK'],))
        sender['QUEUED_MESSAGES'] = []
        sender['MUTED'] = True