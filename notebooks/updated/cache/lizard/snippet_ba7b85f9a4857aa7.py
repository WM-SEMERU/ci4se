def sinusoid(freq, phase=0.0):
    for n in modulo_counter(start=phase, modulo=2 * pi, step=freq):
        yield sin(n)