def user(self):
    return self.users.get(self.contexts[self.current_context].get('user',
        ''), {})