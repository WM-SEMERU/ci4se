def apply_cl_function(cl_function, kernel_data, nmr_instances,
    use_local_reduction=False, cl_runtime_info=None):
    cl_runtime_info = cl_runtime_info or CLRuntimeInfo()
    cl_environments = cl_runtime_info.cl_environments
    for param in cl_function.get_parameters():
        if param.name not in kernel_data:
            names = [param.name for param in cl_function.get_parameters()]
            missing_names = [name for name in names if name not in kernel_data]
            raise ValueError(
                'Some parameters are missing an input value, required parameters are: {}, missing inputs are: {}'
                .format(names, missing_names))
    if cl_function.get_return_type() != 'void':
        kernel_data['_results'] = Zeros((nmr_instances,), cl_function.
            get_return_type())
    workers = []
    for ind, cl_environment in enumerate(cl_environments):
        worker = _ProcedureWorker(cl_environment, cl_runtime_info.
            compile_flags, cl_function, kernel_data, cl_runtime_info.
            double_precision, use_local_reduction)
        workers.append(worker)

    def enqueue_batch(batch_size, offset):
        items_per_worker = [(batch_size // len(cl_environments)) for _ in
            range(len(cl_environments) - 1)]
        items_per_worker.append(batch_size - sum(items_per_worker))
        for ind, worker in enumerate(workers):
            worker.calculate(offset, offset + items_per_worker[ind])
            offset += items_per_worker[ind]
            worker.cl_queue.flush()
        for worker in workers:
            worker.cl_queue.finish()
        return offset
    total_offset = 0
    for batch_start, batch_end in split_in_batches(nmr_instances, 10000.0 *
        len(workers)):
        total_offset = enqueue_batch(batch_end - batch_start, total_offset)
    if cl_function.get_return_type() != 'void':
        return kernel_data['_results'].get_data()