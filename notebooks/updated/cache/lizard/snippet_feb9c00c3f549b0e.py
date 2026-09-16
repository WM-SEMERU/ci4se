def update_text(self, token, match):
    if isinstance(self.text, MatchGroup):
        self.text = self.text.get_group_value(token, match)