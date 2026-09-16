def _validate_templates(self, templates):
    if templates is None:
        return templates
    if not isinstance(templates, list):
        raise TypeError(logger.error('templates should be a list.'))
    for template in templates:
        if not isinstance(template, dict):
            raise TypeError(logger.error(
                'each item to be injected must be a dict.'))
        if template.get('notifications'):
            for level, notification in six.iteritems(template.get(
                'notifications')):
                if level == 'errors':
                    logger.error(
                        'errors were returned during the injection process. errors: {0}'
                        .format(notification), extra={'container': 'injector'})
                    raise Exception(notification)
        for key in ('user', 'name', 'group', 'chmod', 'config_path', 'path',
            'checksum'):
            if key not in template:
                raise KeyError(logger.error(
                    "The injector didn't return a {0}.".format(key)))
    return templates