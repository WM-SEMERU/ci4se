def get_output(db, output_id):
    out = db(
        'SELECT output.*, ds_calc_dir FROM output, job WHERE oq_job_id=job.id AND output.id=?x'
        , output_id, one=True)
    return out.ds_key, out.oq_job_id, os.path.dirname(out.ds_calc_dir)