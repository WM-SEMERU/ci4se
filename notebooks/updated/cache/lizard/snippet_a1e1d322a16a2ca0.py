def qualify(workers, qualification, value, by_name, notify, sandbox):
    if not (workers and qualification and value):
        raise click.BadParameter(
            'Must specify a qualification ID, value/score, and at least one worker ID'
            )
    mturk = _mturk_service_from_config(sandbox)
    if by_name:
        result = mturk.get_qualification_type_by_name(qualification)
        if result is None:
            raise click.BadParameter('No qualification with name "{}" exists.'
                .format(qualification))
        qid = result['id']
    else:
        qid = qualification
    click.echo('Assigning qualification {} with value {} to {} worker{}...'
        .format(qid, value, len(workers), 's' if len(workers) > 1 else ''))
    for worker in workers:
        if mturk.set_qualification_score(qid, worker, int(value), notify=notify
            ):
            click.echo('{} OK'.format(worker))
    results = list(mturk.get_workers_with_qualification(qid))
    click.echo('{} workers with qualification {}:'.format(len(results), qid))
    for score, count in Counter([r['score'] for r in results]).items():
        click.echo('{} with value {}'.format(count, score))