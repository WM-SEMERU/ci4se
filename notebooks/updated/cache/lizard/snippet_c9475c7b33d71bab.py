def stop(id):
    try:
        experiment = ExperimentClient().get(normalize_job_name(id))
    except FloydException:
        experiment = ExperimentClient().get(id)
    if experiment.state not in ['queued', 'queue_scheduled', 'running']:
        floyd_logger.info('Job in {} state cannot be stopped'.format(
            experiment.state))
        sys.exit(1)
    if not ExperimentClient().stop(experiment.id):
        floyd_logger.error('Failed to stop job')
        sys.exit(1)
    floyd_logger.info(
        'Experiment shutdown request submitted. Check status to confirm shutdown'
        )