def doprinc(data):
    ppars = {}
    rad = old_div(np.pi, 180.0)
    X = dir2cart(data)
    T = np.array(Tmatrix(X))
    t, V = tauV(T)
    Pdir = cart2dir(V[0])
    ppars['Edir'] = cart2dir(V[1])
    dec, inc = doflip(Pdir[0], Pdir[1])
    ppars['dec'] = dec
    ppars['inc'] = inc
    ppars['N'] = len(data)
    ppars['tau1'] = t[0]
    ppars['tau2'] = t[1]
    ppars['tau3'] = t[2]
    Pdir = cart2dir(V[1])
    dec, inc = doflip(Pdir[0], Pdir[1])
    ppars['V2dec'] = dec
    ppars['V2inc'] = inc
    Pdir = cart2dir(V[2])
    dec, inc = doflip(Pdir[0], Pdir[1])
    ppars['V3dec'] = dec
    ppars['V3inc'] = inc
    return ppars