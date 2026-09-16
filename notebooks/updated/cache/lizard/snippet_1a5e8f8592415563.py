def changes(ctx, check, dry_run):
    if not dry_run and check not in get_valid_checks():
        abort('Check `{}` is not an Agent-based Integration'.format(check))
    cur_version = get_version_string(check)
    target_tag = get_release_tag_string(check, cur_version)
    diff_lines = get_commits_since(check, target_tag)
    pr_numbers = parse_pr_numbers(diff_lines)
    if not dry_run:
        echo_info('Found {} PRs merged since tag: {}'.format(len(pr_numbers
            ), target_tag))
    user_config = ctx.obj
    if dry_run:
        changelog_types = []
        for pr_num in pr_numbers:
            try:
                payload = get_pr(pr_num, user_config)
            except Exception as e:
                echo_failure('Unable to fetch info for PR #{}: {}'.format(
                    pr_num, e))
                continue
            current_changelog_types = get_changelog_types(payload)
            if not current_changelog_types:
                abort(
                    'No valid changelog labels found attached to PR #{}, please add one!'
                    .format(pr_num))
            elif len(current_changelog_types) > 1:
                abort(
                    'Multiple changelog labels found attached to PR #{}, please only use one!'
                    .format(pr_num))
            current_changelog_type = current_changelog_types[0]
            if current_changelog_type != 'no-changelog':
                changelog_types.append(current_changelog_type)
        return cur_version, changelog_types
    else:
        for pr_num in pr_numbers:
            try:
                payload = get_pr(pr_num, user_config)
            except Exception as e:
                echo_failure('Unable to fetch info for PR #{}: {}'.format(
                    pr_num, e))
                continue
            changelog_types = get_changelog_types(payload)
            echo_success(payload.get('title'))
            echo_info(' * Url: {}'.format(payload.get('html_url')))
            echo_info(' * Changelog status: ', nl=False)
            if not changelog_types:
                echo_warning('WARNING! No changelog labels attached.\n')
            elif len(changelog_types) > 1:
                echo_warning(
                    'WARNING! Too many changelog labels attached: {}\n'.
                    format(', '.join(changelog_types)))
            else:
                echo_success('{}\n'.format(changelog_types[0]))