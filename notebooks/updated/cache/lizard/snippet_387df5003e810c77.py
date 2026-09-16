async def complete_task(context, result):
    args = [get_task_id(context.claim_task), get_run_id(context.claim_task)]
    reversed_statuses = get_reversed_statuses(context)
    try:
        if result == 0:
            log.info('Reporting task complete...')
            response = await context.temp_queue.reportCompleted(*args)
        elif result != 1 and result in reversed_statuses:
            reason = reversed_statuses[result]
            log.info('Reporting task exception {}...'.format(reason))
            payload = {'reason': reason}
            response = await context.temp_queue.reportException(*args, payload)
        else:
            log.info('Reporting task failed...')
            response = await context.temp_queue.reportFailed(*args)
        log.debug('Task status response:\n{}'.format(pprint.pformat(response)))
    except taskcluster.exceptions.TaskclusterRestFailure as exc:
        if exc.status_code == 409:
            log.info('409: not reporting complete/failed.')
        else:
            raise