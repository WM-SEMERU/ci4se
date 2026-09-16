def ansible_verbosity(verbosity):
    previous = display.verbosity
    display.verbosity = verbosity
    yield
    display.verbosity = previous