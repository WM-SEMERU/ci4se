def finish_user(self, subid):
    p = self.revoke_token(subid)
    p.token = 'finished'
    self.session.commit()
    return p