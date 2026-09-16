def par_xstep(i):
    r
    global mp_X
    global mp_DX
    YU0f = sl.rfftn(mp_Y0[[i]] - mp_U0[[i]], mp_Nv, mp_axisN)
    YU1f = sl.rfftn(mp_Y1[mp_grp[i]:mp_grp[i + 1]] - 1 / mp_alpha * mp_U1[
        mp_grp[i]:mp_grp[i + 1]], mp_Nv, mp_axisN)
    if mp_Cd == 1:
        b = np.conj(mp_Df[mp_grp[i]:mp_grp[i + 1]]
            ) * YU0f + mp_alpha ** 2 * YU1f
        Xf = sl.solvedbi_sm(mp_Df[mp_grp[i]:mp_grp[i + 1]], mp_alpha ** 2,
            b, mp_cache[i], axis=mp_axisM)
    else:
        b = sl.inner(np.conj(mp_Df[mp_grp[i]:mp_grp[i + 1]]), YU0f, axis=mp_C
            ) + mp_alpha ** 2 * YU1f
        Xf = sl.solvemdbi_ism(mp_Df[mp_grp[i]:mp_grp[i + 1]], mp_alpha ** 2,
            b, mp_axisM, mp_axisC)
    mp_X[mp_grp[i]:mp_grp[i + 1]] = sl.irfftn(Xf, mp_Nv, mp_axisN)
    mp_DX[i] = sl.irfftn(sl.inner(mp_Df[mp_grp[i]:mp_grp[i + 1]], Xf,
        mp_axisM), mp_Nv, mp_axisN)