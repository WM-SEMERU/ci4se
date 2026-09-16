def do_mode(self, target, msg, nick, send):
    mode_changes = irc.modes.parse_channel_modes(msg)
    with self.data_lock:
        for change in mode_changes:
            if change[1] == 'v':
                self.voiced[target][change[2]] = True if change[0
                    ] == '+' else False
            if change[1] == 'o':
                self.opers[target][change[2]] = True if change[0
                    ] == '+' else False
    if [x for x in mode_changes if self.check_mode(x)]:
        send('%s: :(' % nick, target=target)
        if not self.is_admin(None, nick):
            send('OP %s' % target, target='ChanServ')
            send('UNBAN %s' % target, target='ChanServ')
    if len(self.guarded) > 0:
        regex = '(.*(-v|-o|\\+q|\\+b)[^ ]*) (%s)' % '|'.join(self.guarded)
        match = re.search(regex, msg)
        if match and nick not in [match.group(3), self.connection.real_nickname
            ]:
            modestring = '+voe-qb %s' % ' '.join([match.group(3)] * 5)
            self.connection.mode(target, modestring)
            send('Mode %s on %s by the guard system' % (modestring, target),
                target=self.config['core']['ctrlchan'])