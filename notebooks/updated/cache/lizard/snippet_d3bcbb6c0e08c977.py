def workon(ctx, issue_id, new, base_branch):
    lancet = ctx.obj
    if not issue_id and not new:
        raise click.UsageError('Provide either an issue ID or the --new flag.')
    elif issue_id and new:
        raise click.UsageError(
            'Provide either an issue ID or the --new flag, but not both.')
    if new:
        summary = click.prompt('Issue summary')
        issue = create_issue(lancet, summary=summary, add_to_active_sprint=True
            )
    else:
        issue = get_issue(lancet, issue_id)
    username = lancet.tracker.whoami()
    active_status = lancet.config.get('tracker', 'active_status')
    if not base_branch:
        base_branch = lancet.config.get('repository', 'base_branch')
    branch = get_branch(lancet, issue, base_branch)
    transition = get_transition(ctx, lancet, issue, active_status)
    assign_issue(lancet, issue, username, active_status)
    set_issue_status(lancet, issue, active_status, transition)
    with taskstatus('Checking out working branch') as ts:
        lancet.repo.checkout(branch.name)
        ts.ok('Checked out working branch based on "{}"'.format(base_branch))
    with taskstatus('Starting harvest timer') as ts:
        lancet.timer.start(issue)
        ts.ok('Started harvest timer')