def order_fmap(ncoef):
    loop = True
    order = 1
    while loop:
        loop = not ncoef == ncoef_fmap(order)
        if loop:
            order += 1
            if order > NMAX_ORDER:
                print('No. of coefficients: ', ncoef)
                raise ValueError('order > ' + str(NMAX_ORDER) +
                    ' not implemented')
    return order