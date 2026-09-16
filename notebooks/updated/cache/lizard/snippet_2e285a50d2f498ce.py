def update_model_snapshot(self, job_id, snapshot_id, body, params=None):
    for param in (job_id, snapshot_id, body):
        if param in SKIP_IN_PATH:
            raise ValueError('Empty value passed for a required argument.')
    return self.transport.perform_request('POST', _make_path('_ml',
        'anomaly_detectors', job_id, 'model_snapshots', snapshot_id,
        '_update'), params=params, body=body)