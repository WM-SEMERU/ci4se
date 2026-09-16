def kick(self, member, reason=None):
    yield from self.muc_set_role(member.nick, 'none', reason=reason)