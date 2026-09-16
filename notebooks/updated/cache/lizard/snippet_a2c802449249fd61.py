def get_game(self, name):
    games = self.search_games(query=name, live=False)
    for g in games:
        if g.name == name:
            return g