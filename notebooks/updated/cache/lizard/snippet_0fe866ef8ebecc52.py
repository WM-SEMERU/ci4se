def __proxy_status(self, job_directory, job_id):
    state_change = None
    if job_directory.has_metadata(JOB_FILE_PREPROCESSING_FAILED):
        proxy_status = status.FAILED
        job_directory.store_metadata(JOB_FILE_FINAL_STATUS, proxy_status)
        state_change = 'to_complete'
    elif not job_directory.has_metadata(JOB_FILE_PREPROCESSED):
        proxy_status = status.PREPROCESSING
    elif job_directory.has_metadata(JOB_FILE_FINAL_STATUS):
        proxy_status = job_directory.load_metadata(JOB_FILE_FINAL_STATUS)
    else:
        proxy_status = self._proxied_manager.get_status(job_id)
        if proxy_status == status.RUNNING:
            if not job_directory.has_metadata(JOB_METADATA_RUNNING):
                job_directory.store_metadata(JOB_METADATA_RUNNING, True)
                state_change = 'to_running'
        elif proxy_status in [status.COMPLETE, status.CANCELLED]:
            job_directory.store_metadata(JOB_FILE_FINAL_STATUS, proxy_status)
            state_change = 'to_complete'
    return proxy_status, state_change