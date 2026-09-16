def ellplot(mjr, mnr, pa):
    _ellcheck(mjr, mnr, pa)
    import omega as om
    th = np.linspace(0, 2 * np.pi, 200)
    x, y = ellpoint(mjr, mnr, pa, th)
    return om.quickXY(x, y, 'mjr=%f mnr=%f pa=%f' % (mjr, mnr, pa * 180 /
        np.pi))