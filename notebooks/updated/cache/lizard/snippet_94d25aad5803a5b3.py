def dok15_s(k15):
    A, B = design(15)
    sbar = np.dot(B, k15)
    t = sbar[0] + sbar[1] + sbar[2]
    bulk = old_div(t, 3.0)
    Kbar = np.dot(A, sbar)
    dels = k15 - Kbar
    dels, sbar = old_div(dels, t), old_div(sbar, t)
    So = sum(dels ** 2)
    sigma = np.sqrt(old_div(So, 9.0))
    return sbar, sigma, bulk