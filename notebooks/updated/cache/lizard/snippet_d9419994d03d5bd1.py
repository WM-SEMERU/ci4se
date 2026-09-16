def is_projector(operator):
    return is_hermitian(operator) and (operator * operator - operator).norm(
        FROBENIUS) / operator.norm(FROBENIUS) < EPS