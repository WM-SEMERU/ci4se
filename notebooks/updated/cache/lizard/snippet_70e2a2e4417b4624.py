def update_payload(self, fields=None):
    payload = super(JobTemplate, self).update_payload(fields)
    effective_user = payload.pop('effective_user', None)
    if effective_user:
        payload['ssh'] = {'effective_user': effective_user}
    return {'job_template': payload}