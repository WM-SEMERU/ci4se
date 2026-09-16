def sync(ctx, scm, to_branch, verbose, fake):
    scm.fake = fake
    scm.verbose = fake or verbose
    scm.repo_check(require_remote=True)
    if to_branch:
        branch = scm.fuzzy_match_branch(to_branch)
        if branch:
            is_external = True
            original_branch = scm.get_current_branch_name()
        else:
            raise click.BadArgumentUsage(
                'Branch {0} does not exist. Use an existing branch.'.format
                (crayons.yellow(branch)))
    else:
        branch = scm.get_current_branch_name()
        is_external = False
    if branch in scm.get_branch_names(local=False):
        if is_external:
            ctx.invoke(switch, to_branch=branch, verbose=verbose, fake=fake)
        scm.stash_log(sync=True)
        status_log(scm.smart_pull, 'Pulling commits from the server.')
        status_log(scm.push, 'Pushing commits to the server.', branch)
        scm.unstash_log(sync=True)
        if is_external:
            ctx.invoke(switch, to_branch=original_branch, verbose=verbose,
                fake=fake)
    else:
        raise click.BadArgumentUsage(
            'Branch {0} is not published. Publish before syncing.'.format(
            crayons.yellow(branch)))