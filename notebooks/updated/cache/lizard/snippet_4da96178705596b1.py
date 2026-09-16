def mark_job_as_completed(job_id, data=None):
    update_dict = {'status': 'complete', 'data': json.dumps(data),
        'finished_timestamp': datetime.datetime.now()}
    _update_job(job_id, update_dict)