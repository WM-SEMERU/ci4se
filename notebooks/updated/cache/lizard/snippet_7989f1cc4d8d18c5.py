def plus_dora(tile, dora_indicators):
    tile_index = tile // 4
    dora_count = 0
    for dora in dora_indicators:
        dora //= 4
        if tile_index < EAST:
            if dora == 8:
                dora = -1
            elif dora == 17:
                dora = 8
            elif dora == 26:
                dora = 17
            if tile_index == dora + 1:
                dora_count += 1
        else:
            if dora < EAST:
                continue
            dora -= 9 * 3
            tile_index_temp = tile_index - 9 * 3
            if dora == 3:
                dora = -1
            if dora == 6:
                dora = 3
            if tile_index_temp == dora + 1:
                dora_count += 1
    return dora_count