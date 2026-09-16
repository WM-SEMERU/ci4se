def prepare_run(run_id, run_data):
    idf, kwargs = run_data
    epw = idf.epw
    idf_dir = os.path.join('multi_runs', 'idf_%i' % run_id)
    os.mkdir(idf_dir)
    idf_path = os.path.join(idf_dir, 'in.idf')
    idf.saveas(idf_path)
    return (idf_path, epw), kwargs