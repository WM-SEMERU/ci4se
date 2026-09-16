def build_sample_ace_problem_breiman2(N=500):
    x = numpy.linspace(0, 1, N)
    noise = numpy.random.standard_normal(N)
    y = numpy.exp(numpy.sin(2 * numpy.pi * x)) + 0.0 * noise
    return [x], y