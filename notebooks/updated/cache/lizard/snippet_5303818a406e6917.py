def _actor_from_game_image(self, name, game_image):
    HEALTH_MAX = 100
    MANA_MAX = 40
    tools = {'player': self._player_tools, 'opponent': self._oppnt_tools}[name]
    args = [name]
    t, l, b, r = tools['health_region'].region_in(game_image)
    health_image = game_image[t:b, l:r]
    health_image = numpy.rot90(health_image)
    how_full = tools['health_tank'].how_full(health_image)
    if how_full is None:
        return None
    health = int(round(HEALTH_MAX * how_full))
    args.append((health, HEALTH_MAX))
    for color in ('r', 'g', 'b', 'y'):
        t, l, b, r = tools[color + '_region'].region_in(game_image)
        mana_image = game_image[t:b, l:r]
        how_full = tools[color + '_tank'].how_full(mana_image)
        if how_full is None:
            return None
        mana = int(round(MANA_MAX * how_full))
        args.append((mana, MANA_MAX))
    x_m = (0, 1000), (0, 1000)
    args.extend(x_m)
    h_c = (0, 0), (0, 0)
    args.extend(h_c)
    return Actor(*args)