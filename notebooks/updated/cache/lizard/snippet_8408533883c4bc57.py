def check_anagrad(fun, x0, epsilon, threshold):
    N = len(x0)
    f0, ana_grad = fun(x0, do_gradient=True)
    for i in range(N):
        xh = x0.copy()
        xh[i] += 0.5 * epsilon
        xl = x0.copy()
        xl[i] -= 0.5 * epsilon
        num_grad_comp = (fun(xh) - fun(xl)) / epsilon
        if abs(num_grad_comp - ana_grad[i]) > threshold:
            raise AssertionError(
                'Error in the analytical gradient, component %i, got %s, should be about %s'
                 % (i, ana_grad[i], num_grad_comp))