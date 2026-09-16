def score_wu(CIJ, s):
    CIJscore = CIJ.copy()
    while True:
        str = strengths_und(CIJscore)
        ff, = np.where(np.logical_and(str < s, str > 0))
        if ff.size == 0:
            break
        CIJscore[(ff), :] = 0
        CIJscore[:, (ff)] = 0
    sn = np.sum(str > 0)
    return CIJscore, sn