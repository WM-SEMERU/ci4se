def __job_complete_dict(complete_status, manager, job_id):
    return_code = manager.return_code(job_id)
    if return_code == PULSAR_UNKNOWN_RETURN_CODE:
        return_code = None
    stdout_contents = manager.stdout_contents(job_id).decode('utf-8')
    stderr_contents = manager.stderr_contents(job_id).decode('utf-8')
    job_directory = manager.job_directory(job_id)
    as_dict = dict(job_id=job_id, complete='true', status=complete_status,
        returncode=return_code, stdout=stdout_contents, stderr=
        stderr_contents, working_directory=job_directory.working_directory(
        ), metadata_directory=job_directory.metadata_directory(),
        working_directory_contents=job_directory.working_directory_contents
        (), metadata_directory_contents=job_directory.
        metadata_directory_contents(), outputs_directory_contents=
        job_directory.outputs_directory_contents(), system_properties=
        manager.system_properties(), pulsar_version=pulsar_version)
    return as_dict