def hex_to_rgb(color):
    color = normalize(color)
    color = color[1:]
    return 'rgb' + str((int(color[0:2], base=16), int(color[2:4], base=16),
        int(color[4:6], base=16)))