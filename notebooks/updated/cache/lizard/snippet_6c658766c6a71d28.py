def get_most_specific_tinfo(goids, go2nt):
    return max(_get_go2nt(goids, go2nt), key=lambda t: t[1].tinfo)[0]