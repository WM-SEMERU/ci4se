def checkSquareStochastic(matrix):
    if not isSquare(matrix):
        raise _error.SquareError
    if not isStochastic(matrix):
        raise _error.StochasticError
    if not isNonNegative(matrix):
        raise _error.NonNegativeError