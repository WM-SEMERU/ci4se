def _pull_assemble_error_status(logs):
    comment = 'An error occurred pulling your image'
    try:
        for err_log in logs:
            if isinstance(err_log, dict):
                if 'errorDetail' in err_log:
                    if 'code' in err_log['errorDetail']:
                        msg = '\n{0}\n{1}: {2}'.format(err_log['error'],
                            err_log['errorDetail']['code'], err_log[
                            'errorDetail']['message'])
                    else:
                        msg = '\n{0}\n{1}'.format(err_log['error'], err_log
                            ['errorDetail']['message'])
                    comment += msg
    except Exception as e:
        comment += '%s' % e
    return comment