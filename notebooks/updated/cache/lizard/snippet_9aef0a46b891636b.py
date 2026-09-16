def detrend(self, method='linear', order=5):
    check_options(method, ['linear', 'nonlinear'])
    if method == 'linear':
        order = 1

    def func(y):
        x = arange(len(y))
        p = polyfit(x, y, order)
        p[-1] = 0
        yy = polyval(p, x)
        return y - yy
    return self.map(func)