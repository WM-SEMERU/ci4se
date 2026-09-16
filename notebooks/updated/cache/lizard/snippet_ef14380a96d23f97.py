def estimate_lambda(pv):
    LOD2 = sp.median(st.chi2.isf(pv, 1))
    L = LOD2 / 0.456
    return L