def genlet(generator_function=None, prime=True):
    if generator_function is None:
        return GeneratorLink.wraplet(prime=prime)
    elif not callable(generator_function):
        return GeneratorLink.wraplet(prime=generator_function)
    return GeneratorLink.wraplet(prime=prime)(generator_function)