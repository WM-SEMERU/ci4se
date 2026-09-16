def players(self, postgame, game_type):
    for i, attributes in self._players():
        yield self._parse_player(i, attributes, postgame, game_type)