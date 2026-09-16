def create_kernel_instance(self, kernel_options, params, verbose):
    instance_string = util.get_instance_string(params)
    grid_div = (kernel_options.grid_div_x, kernel_options.grid_div_y,
        kernel_options.grid_div_z)
    if not kernel_options.block_size_names:
        kernel_options.block_size_names = util.default_block_size_names
    threads, grid = util.setup_block_and_grid(kernel_options.problem_size,
        grid_div, params, kernel_options.block_size_names)
    if numpy.prod(threads) > self.dev.max_threads:
        if verbose:
            print('skipping config', instance_string,
                'reason: too many threads per block')
        return None
    temp_files = dict()
    kernel_source = kernel_options.kernel_string
    if not isinstance(kernel_source, list):
        kernel_source = [kernel_source]
    name, kernel_string, temp_files = util.prepare_list_of_files(kernel_options
        .kernel_name, kernel_source, params, grid, threads, kernel_options.
        block_size_names)
    return KernelInstance(name, kernel_string, temp_files, threads, grid,
        params, kernel_options.arguments)