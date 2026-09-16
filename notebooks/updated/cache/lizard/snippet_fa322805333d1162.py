def updatePlayer(name, settings):
    player = delPlayer(name)
    _validate(settings)
    player.update(settings)
    player.save()
    getKnownPlayers()[player.name] = player
    return player