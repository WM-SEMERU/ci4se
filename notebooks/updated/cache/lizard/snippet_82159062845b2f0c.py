def _build_ref_data_names(self, project, build_system):
    ignored_jobs = []
    ref_data_names = {}
    runnable_jobs = list_runnable_jobs(project)
    for job in runnable_jobs:
        testtype = parse_testtype(build_system_type=job['build_system_type'
            ], job_type_name=job['job_type_name'], platform_option=job[
            'platform_option'], ref_data_name=job['ref_data_name'])
        if not valid_platform(job['platform']):
            continue
        if is_job_blacklisted(testtype):
            ignored_jobs.append(job['ref_data_name'])
            continue
        key = unique_key(testtype=testtype, buildtype=job['platform_option'
            ], platform=job['platform'])
        if build_system == '*':
            ref_data_names[key] = job['ref_data_name']
        elif job['build_system_type'] == build_system:
            ref_data_names[key] = job['ref_data_name']
    for ref_data_name in sorted(ignored_jobs):
        logger.info('Ignoring %s', ref_data_name)
    return ref_data_names