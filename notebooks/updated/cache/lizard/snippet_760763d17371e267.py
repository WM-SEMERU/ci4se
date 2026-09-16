def build_board_checkers():
    grd = Grid(8, 8, ['B', 'W'])
    for c in range(4):
        grd.set_tile(0, c * 2 - 1, 'B')
        grd.set_tile(1, c * 2 - 0, 'B')
        grd.set_tile(6, c * 2 + 1, 'W')
        grd.set_tile(7, c * 2 - 0, 'W')
    print(grd)
    return grd