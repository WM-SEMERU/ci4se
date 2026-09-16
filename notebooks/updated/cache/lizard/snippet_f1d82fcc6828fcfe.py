def load(self):
    user_profile = self.session.session.get(
        'http://myanimelist.net/profile/' + utilities.urlencode(self.username)
        ).text
    self.set(self.parse(utilities.get_clean_dom(user_profile)))
    return self