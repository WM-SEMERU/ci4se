def toRanks(A):
    AA = sp.zeros_like(A)
    for i in range(A.shape[1]):
        AA[:, (i)] = st.rankdata(A[:, (i)])
    AA = sp.array(sp.around(AA), dtype='int') - 1
    return AA