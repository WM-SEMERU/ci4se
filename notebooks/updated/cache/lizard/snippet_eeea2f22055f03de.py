def crt(self, mp, mq):
    u = (mq - mp) * self.p_inverse % self.q
    return mp + u * self.p