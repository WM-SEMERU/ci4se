def output_summary(fqn, action, changeset, params_diff, replacements_only=False
    ):
    replacements = []
    changes = []
    for change in changeset:
        resource = change['ResourceChange']
        replacement = resource.get('Replacement') == 'True'
        summary = '- %s %s (%s)' % (resource['Action'], resource[
            'LogicalResourceId'], resource['ResourceType'])
        if replacement:
            replacements.append(summary)
        else:
            changes.append(summary)
    summary = ''
    if params_diff:
        summary += summarize_params_diff(params_diff)
    if replacements:
        if not replacements_only:
            summary += 'Replacements:\n'
        summary += '\n'.join(replacements)
    if changes:
        if summary:
            summary += '\n'
        summary += 'Changes:\n%s' % '\n'.join(changes)
    logger.info('%s %s:\n%s', fqn, action, summary)