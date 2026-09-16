def check_nonparametric_sources(fname, smodel, investigation_time):
    np = [src for sg in smodel.src_groups for src in sg if hasattr(src, 'data')
        ]
    if np and smodel.investigation_time != investigation_time:
        raise ValueError(
            'The source model %s contains an investigation_time of %s, while the job.ini has %s'
             % (fname, smodel.investigation_time, investigation_time))
    return np