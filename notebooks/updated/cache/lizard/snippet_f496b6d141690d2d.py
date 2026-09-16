def delete_job(self, job_id, params=None):
    if job_id in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'job_id'."
            )
    return self.transport.perform_request('DELETE', _make_path('_ml',
        'anomaly_detectors', job_id), params=params)