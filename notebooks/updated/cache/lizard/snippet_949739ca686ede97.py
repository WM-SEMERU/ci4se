def check_for_completion(self):
    job_result_obj = self.session.get(self.uri)
    job_status = job_result_obj['status']
    if job_status == 'complete':
        self.session.delete(self.uri)
        op_status_code = job_result_obj['job-status-code']
        if op_status_code in (200, 201):
            op_result_obj = job_result_obj.get('job-results', None)
        elif op_status_code == 204:
            op_result_obj = None
        else:
            error_result_obj = job_result_obj.get('job-results', None)
            if not error_result_obj:
                message = None
            elif 'message' in error_result_obj:
                message = error_result_obj['message']
            elif 'error' in error_result_obj:
                message = error_result_obj['error']
            else:
                message = None
            error_obj = {'http-status': op_status_code, 'reason':
                job_result_obj['job-reason-code'], 'message': message,
                'request-method': self.op_method, 'request-uri': self.op_uri}
            raise HTTPError(error_obj)
    else:
        op_result_obj = None
    return job_status, op_result_obj