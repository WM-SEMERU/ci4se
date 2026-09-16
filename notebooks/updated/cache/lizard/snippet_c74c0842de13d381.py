def make_color_tuple(color):
    R = color[1:3]
    G = color[3:5]
    B = color[5:7]
    R = int(R, 16)
    G = int(G, 16)
    B = int(B, 16)
    return R, G, B