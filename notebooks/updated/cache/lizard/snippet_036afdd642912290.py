def locate_bar_r(icut, epos):
    sm = len(icut)

    def swap_coor(x):
        return sm - 1 - x

    def swap_line(tab):
        return tab[::-1]
    return _locate_bar_gen(icut, epos, transform1=swap_coor, transform2=
        swap_line)