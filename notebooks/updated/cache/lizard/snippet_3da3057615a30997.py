def copy_table(self, sources, destination, job_id=None, job_id_prefix=None,
    location=None, project=None, job_config=None, retry=DEFAULT_RETRY):
    job_id = _make_job_id(job_id, job_id_prefix)
    if project is None:
        project = self.project
    if location is None:
        location = self.location
    job_ref = job._JobReference(job_id, project=project, location=location)
    sources = _table_arg_to_table_ref(sources, default_project=self.project)
    if not isinstance(sources, collections_abc.Sequence):
        sources = [sources]
    sources = [_table_arg_to_table_ref(source, default_project=self.project
        ) for source in sources]
    destination = _table_arg_to_table_ref(destination, default_project=self
        .project)
    copy_job = job.CopyJob(job_ref, sources, destination, client=self,
        job_config=job_config)
    copy_job._begin(retry=retry)
    return copy_job