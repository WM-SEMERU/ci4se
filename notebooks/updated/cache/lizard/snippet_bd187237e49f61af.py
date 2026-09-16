def save_to_npy_file(self, parameter_space, result_parsing_function,
    filename, runs):
    np.save(filename, self.get_results_as_numpy_array(parameter_space,
        result_parsing_function, runs=runs))