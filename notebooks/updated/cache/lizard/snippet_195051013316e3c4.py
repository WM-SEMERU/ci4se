def get_messages(self):
    cs = self.data['comments']['data']
    res = []
    for c in cs:
        res.append(Message(c, self))
    return res