def sprite(map, sprite, offset_x=None, offset_y=None, cache_buster=True):
    map = map.render()
    sprite_maps = _get_cache('sprite_maps')
    sprite_map = sprite_maps.get(map)
    sprite_name = String.unquoted(sprite).value
    sprite = sprite_map and sprite_map.get(sprite_name)
    if not sprite_map:
        log.error('No sprite map found: %s', map, extra={'stack': True})
    elif not sprite:
        log.error('No sprite found: %s in %s', sprite_name, sprite_map[
            '*n*'], extra={'stack': True})
    if sprite:
        url = '%s%s' % (config.ASSETS_URL, sprite_map['*f*'])
        if cache_buster:
            url += '?_=%s' % sprite_map['*t*']
        x = Number(offset_x or 0, 'px')
        y = Number(offset_y or 0, 'px')
        if not x.value or (x.value <= -1 or x.value >= 1
            ) and not x.is_simple_unit('%'):
            x -= Number(sprite[2], 'px')
        if not y.value or (y.value <= -1 or y.value >= 1
            ) and not y.is_simple_unit('%'):
            y -= Number(sprite[3], 'px')
        url = 'url(%s)' % escape(url)
        return List([String.unquoted(url), x, y])
    return List([Number(0), Number(0)])