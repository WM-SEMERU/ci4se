def norm(x, y=None, ip_B=None):
    r
    if y is None and (ip_B is None or isinstance(ip_B, IdentityLinearOperator)
        ):
        return numpy.linalg.norm(x, 2)
    if y is None:
        y = x
    ip = inner(x, y, ip_B=ip_B)
    nrm_diag = numpy.linalg.norm(numpy.diag(ip), 2)
    nrm_diag_imag = numpy.linalg.norm(numpy.imag(numpy.diag(ip)), 2)
    if nrm_diag_imag > nrm_diag * 1e-10:
        raise InnerProductError(
            'inner product defined by ip_B not positive definite? ||diag(ip).imag||/||diag(ip)||={0}'
            .format(nrm_diag_imag / nrm_diag))
    return numpy.sqrt(numpy.linalg.norm(ip, 2))