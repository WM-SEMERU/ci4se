def inflate(self, newData={}):
    from sc2maptool.functions import selectMap
    from sc2maptool.mapRecord import MapRecord
    self.__dict__.update(newData)
    if self.expo and not isinstance(self.expo, types.ExpansionNames):
        self.expo = types.ExpansionNames(self.expo)
    if self.version and not isinstance(self.version, versions.Version):
        self.version = versions.Version(self.version)
    if self.ladder and not isinstance(self.ladder, Ladder):
        self.ladder = Ladder(self.ladder)
    for i, player in enumerate(self.players):
        if isinstance(player, str):
            self.players[i] = getPlayer(player)
        elif not isinstance(player, PlayerRecord):
            self.players[i] = buildPlayer(*player)
    if self.mode and not isinstance(self.mode, types.GameModes):
        self.mode = types.GameModes(self.mode)
    if self.themap and not isinstance(self.themap, MapRecord):
        self.themap = selectMap(name=self.themap)