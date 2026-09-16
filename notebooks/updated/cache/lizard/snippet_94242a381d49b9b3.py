def ask_for_approval(full_changeset=None, params_diff=None, include_verbose
    =False):
    approval_options = ['y', 'n']
    if include_verbose:
        approval_options.append('v')
    approve = ui.ask('Execute the above changes? [{}] '.format('/'.join(
        approval_options))).lower()
    if include_verbose and approve == 'v':
        if params_diff:
            logger.info('Full changeset:\n\n%s\n%s', format_params_diff(
                params_diff), yaml.safe_dump(full_changeset))
        else:
            logger.info('Full changeset:\n%s', yaml.safe_dump(full_changeset))
        return ask_for_approval()
    elif approve != 'y':
        raise exceptions.CancelExecution