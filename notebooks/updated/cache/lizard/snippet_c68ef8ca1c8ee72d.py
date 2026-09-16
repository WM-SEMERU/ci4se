def delete(self, name, action, seqno):
    return self.configure('no route-map %s %s %s' % (name, action, seqno))