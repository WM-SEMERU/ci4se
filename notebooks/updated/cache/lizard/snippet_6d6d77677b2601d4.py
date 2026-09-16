def runIDFs(jobs, processors=1):
    if processors <= 0:
        processors = max(1, mp.cpu_count() - processors)
    shutil.rmtree('multi_runs', ignore_errors=True)
    os.mkdir('multi_runs')
    prepared_runs = (prepare_run(run_id, run_data) for run_id, run_data in
        enumerate(jobs))
    try:
        pool = mp.Pool(processors)
        pool.map(multirunner, prepared_runs)
        pool.close()
    except NameError:
        for job in prepared_runs:
            multirunner([job])
    shutil.rmtree('multi_runs', ignore_errors=True)