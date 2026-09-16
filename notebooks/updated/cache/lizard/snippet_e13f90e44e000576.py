def do_some_work(self, work_dict):
    label = 'do_some_work'
    log.info('task - {} - start work_dict={}'.format(label, work_dict))
    ret_data = {'job_results': 'some response key={}'.format(str(uuid.uuid4()))
        }
    log.info('task - {} - result={} done'.format(ret_data, label))
    return ret_data