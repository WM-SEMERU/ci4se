def assignValue(cfg, playerValue, otherValue):
    player = cfg.whoAmI()
    result = {}
    for p in cfg.players:
        if p.name == player.name:
            val = playerValue
        else:
            val = otherValue
        result[p.name] = val
    return result