def add_job(session, command_line, name='job', dependencies=[], array=None,
    exec_dir=None, log_dir=None, stop_on_failure=False, **kwargs):
    job = Job(command_line=command_line, name=name, exec_dir=exec_dir,
        log_dir=log_dir, array_string=array, stop_on_failure=
        stop_on_failure, kwargs=kwargs)
    session.add(job)
    session.flush()
    session.refresh(job)
    job.id = job.unique
    for d in dependencies:
        if d == job.unique:
            logger.warn('Adding self-dependency of job %d is not allowed' % d)
            continue
        depending = list(session.query(Job).filter(Job.unique == d))
        if len(depending):
            session.add(JobDependence(job.unique, depending[0].unique))
        else:
            logger.warn(
                'Could not find dependent job with id %d in database' % d)
    if array:
        start, stop, step = array
        for i in range(start, stop + 1, step):
            session.add(ArrayJob(i, job.unique))
    session.commit()
    return job