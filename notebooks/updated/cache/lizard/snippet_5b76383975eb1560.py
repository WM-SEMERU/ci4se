def run(self, grid=None, num_of_paths=2000, seed=0, num_of_workers=
    CPU_COUNT, profiling=False):
    self.grid = sorted(set(grid))
    self.num_of_paths = num_of_paths
    self.num_of_workers = num_of_workers
    self.seed = seed
    self.producer.initialize(self.grid, self.num_of_paths, self.seed)
    self.consumer.initialize(self.grid, self.num_of_paths, self.seed)
    if num_of_workers:
        workers = list()
        queue = Queue()
        path_per_worker = int(num_of_paths // num_of_workers)
        start_path, stop_path = 0, path_per_worker
        for i in range(num_of_workers):
            if i == num_of_workers - 1:
                stop_path = num_of_paths
            name = 'worker-%d' % i
            if profiling:
                workers.append(Process(target=self.
                    _run_parallel_process_with_profiling, name=name, args=(
                    start_path, stop_path, queue, name + '.prof')))
            else:
                workers.append(Process(target=self._run_parallel_process,
                    name=name, args=(start_path, stop_path, queue)))
            start_path, stop_path = stop_path, stop_path + path_per_worker
        for worker in workers:
            worker.start()
        for _ in range(num_of_workers):
            self.consumer.get(queue.get())
        for worker in workers:
            worker.join()
    else:
        self._run_process(0, num_of_paths)
    self.consumer.finalize()
    return self.consumer.result