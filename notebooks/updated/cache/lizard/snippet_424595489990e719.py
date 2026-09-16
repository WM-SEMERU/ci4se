def synthetic_grad(X, theta, sigma1, sigma2, sigmax, rescale_grad=1.0, grad
    =None):
    if grad is None:
        grad = nd.empty(theta.shape, theta.context)
    theta1 = theta.asnumpy()[0]
    theta2 = theta.asnumpy()[1]
    v1 = sigma1 ** 2
    v2 = sigma2 ** 2
    vx = sigmax ** 2
    denominator = numpy.exp(-(X - theta1) ** 2 / (2 * vx)) + numpy.exp(-(X -
        theta1 - theta2) ** 2 / (2 * vx))
    grad_npy = numpy.zeros(theta.shape)
    grad_npy[0] = -rescale_grad * ((numpy.exp(-(X - theta1) ** 2 / (2 * vx)
        ) * (X - theta1) / vx + numpy.exp(-(X - theta1 - theta2) ** 2 / (2 *
        vx)) * (X - theta1 - theta2) / vx) / denominator).sum() + theta1 / v1
    grad_npy[1] = -rescale_grad * (numpy.exp(-(X - theta1 - theta2) ** 2 /
        (2 * vx)) * (X - theta1 - theta2) / vx / denominator).sum(
        ) + theta2 / v2
    grad[:] = grad_npy
    return grad