def line_segment(X0, X1):
    r
    X0 = sp.around(X0).astype(int)
    X1 = sp.around(X1).astype(int)
    if len(X0) == 3:
        L = sp.amax(sp.absolute([[X1[0] - X0[0]], [X1[1] - X0[1]], [X1[2] -
            X0[2]]])) + 1
        x = sp.rint(sp.linspace(X0[0], X1[0], L)).astype(int)
        y = sp.rint(sp.linspace(X0[1], X1[1], L)).astype(int)
        z = sp.rint(sp.linspace(X0[2], X1[2], L)).astype(int)
        return [x, y, z]
    else:
        L = sp.amax(sp.absolute([[X1[0] - X0[0]], [X1[1] - X0[1]]])) + 1
        x = sp.rint(sp.linspace(X0[0], X1[0], L)).astype(int)
        y = sp.rint(sp.linspace(X0[1], X1[1], L)).astype(int)
        return [x, y]