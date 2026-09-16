def flightmode_menu():
    global flightmodes
    ret = []
    idx = 0
    for mode, t1, t2 in flightmodes:
        modestr = '%s %us' % (mode, t2 - t1)
        ret.append(MPMenuCheckbox(modestr, modestr, 'mode-%u' % idx))
        idx += 1
        mestate.flightmode_selections.append(False)
    return ret