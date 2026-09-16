def get_conversations(self):
    cs = self.data['data']
    res = []
    for c in cs:
        res.append(Conversation(c))
    return res