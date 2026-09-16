def cases(ctx, case_id, to_json):
    adapter = ctx.obj['adapter']
    cases = []
    if case_id:
        case_obj = adapter.case({'case_id': case_id})
        if not case_obj:
            LOG.info('Case {0} does not exist in database'.format(case_id))
            return
        case_obj['_id'] = str(case_obj['_id'])
        cases.append(case_obj)
    else:
        cases = adapter.cases()
        if cases.count() == 0:
            LOG.info('No cases found in database')
            ctx.abort()
    if to_json:
        click.echo(json.dumps(cases))
        return
    click.echo('#case_id\tvcf_path')
    for case_obj in cases:
        click.echo('{0}\t{1}'.format(case_obj.get('case_id'), case_obj.get(
            'vcf_path')))