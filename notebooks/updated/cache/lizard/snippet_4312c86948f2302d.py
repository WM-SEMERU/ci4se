def badnick(self, me=None, nick=None, **kw):
    if me == '*':
        self.bot.set_nick(self.bot.nick + '_')
    self.bot.log.debug('Trying to regain nickname in 30s...')
    self.nick_handle = self.bot.loop.call_later(30, self.bot.set_nick, self
        .bot.original_nick)