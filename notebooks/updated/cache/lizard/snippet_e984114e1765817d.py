def adapt_input_for_backend(self, input_data):
    for problem in self._problems:
        input_data = problem.adapt_input_for_backend(input_data)
    return input_data