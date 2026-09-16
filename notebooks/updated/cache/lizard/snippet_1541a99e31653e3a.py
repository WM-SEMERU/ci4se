def color_to_tuple(color, opacity=1):
    if type(color) == str and color[0] == '#':
        color = hex_color_to_tuple(color)
    elif type(color) == str:
        if color in color_dict:
            color = color_dict[color.lower()]
        else:
            print('无法解析颜色:' + color)
            color = 255, 125, 0, int(255 * opacity)
    while len(color) < 4:
        color += int(255 * opacity),
    return color