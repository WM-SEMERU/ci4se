def linreg(x, y):
    if len(x) != len(y):
        print('x and y must be same length')
        return
    xx, yy, xsum, ysum, xy, n, sum = 0, 0, 0, 0, 0, len(x), 0
    linpars = {}
    for i in range(n):
        xx += x[i] * x[i]
        yy += y[i] * y[i]
        xy += x[i] * y[i]
        xsum += x[i]
        ysum += y[i]
        xsig = np.sqrt(old_div(xx - old_div(xsum ** 2, n), n - 1.0))
        ysig = np.sqrt(old_div(yy - old_div(ysum ** 2, n), n - 1.0))
    linpars['slope'] = old_div(xy - xsum * ysum / n, xx - old_div(xsum ** 2, n)
        )
    linpars['b'] = old_div(ysum - linpars['slope'] * xsum, n)
    linpars['r'] = old_div(linpars['slope'] * xsig, ysig)
    for i in range(n):
        a = y[i] - linpars['b'] - linpars['slope'] * x[i]
        sum += a
    linpars['sigma'] = old_div(sum, n - 2.0)
    linpars['n'] = n
    return linpars