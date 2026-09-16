def run_parallel(workflow, n_threads):
    scheduler = Scheduler()
    threaded_worker = Queue() >> thread_pool(*repeat(worker, n_threads))
    return scheduler.run(threaded_worker, get_workflow(workflow))