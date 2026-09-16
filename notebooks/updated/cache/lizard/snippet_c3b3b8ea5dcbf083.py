def idPlayerResults(cfg, rawResult):
    result = {}
    knownPlayers = []
    dictResult = {plyrRes.player_id: plyrRes.result for plyrRes in rawResult}
    for p in cfg.players:
        if p.playerID and p.playerID in dictResult:
            knownPlayers.append(p)
            result[p.name] = dictResult[p.playerID]
    return result