def get_history_tags(self, exp, rep=0):
    history = self.get_history(exp, rep, 'all')
    return history.keys()