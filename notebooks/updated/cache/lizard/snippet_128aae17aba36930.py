def update_stack(self, fqn, template, old_parameters, parameters, tags,
    force_interactive=False, force_change_set=False, stack_policy=None, **
    kwargs):
    logger.debug('Attempting to update stack %s:', fqn)
    logger.debug('    parameters: %s', parameters)
    logger.debug('    tags: %s', tags)
    if template.url:
        logger.debug('    template_url: %s', template.url)
    else:
        logger.debug('    no template url, uploading template directly.')
    update_method = self.select_update_method(force_interactive,
        force_change_set)
    return update_method(fqn, template, old_parameters, parameters,
        stack_policy=stack_policy, tags=tags, **kwargs)