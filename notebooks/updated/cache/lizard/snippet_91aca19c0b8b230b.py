def data(ctx, path):
    _rws = partial(rws_call, ctx)
    if len(path) == 0:
        _rws(ClinicalStudiesRequest(), default_attr='oid')
    elif len(path) == 1:
        _rws(StudySubjectsRequest(path[0], 'Prod'), default_attr='subjectkey')
    elif len(path) == 2:
        _rws(StudySubjectsRequest(path[0], path[1]), default_attr='subjectkey')
    elif len(path) == 3:
        try:
            click.echo(get_data(ctx, path[0], path[1], path[2]))
        except RWSException as e:
            click.echo(str(e))
        except requests.exceptions.HTTPError as e:
            click.echo(str(e))
    else:
        click.echo('Too many arguments')