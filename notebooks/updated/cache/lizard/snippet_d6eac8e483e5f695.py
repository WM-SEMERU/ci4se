def create(cls, **kwargs):
    linkname = kwargs.setdefault('linkname', cls.clientclass.linkname_default)
    job_archive = kwargs.get('job_archive', None)
    if job_archive is None:
        job_archive = JobArchive.build_temp_job_archive()
        kwargs.setdefault('job_archive', job_archive)
    kwargs_client = dict(linkname=linkname, link_prefix=kwargs.get(
        'link_prefix', ''), file_stage=kwargs.get('file_stage', None),
        job_archive=job_archive)
    link = cls.clientclass.create(**kwargs_client)
    sg = cls(link, **kwargs)
    return sg