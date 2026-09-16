def restart(gandi, resource, background, force):
    output_keys = ['id', 'type', 'step']
    possible_resources = gandi.paas.resource_list()
    for item in resource:
        if item not in possible_resources:
            gandi.echo('Sorry PaaS instance %s does not exist' % item)
            gandi.echo('Please use one of the following: %s' %
                possible_resources)
            return
    if not force:
        instance_info = "'%s'" % ', '.join(resource)
        proceed = click.confirm('Are you sure to restart PaaS instance %s?' %
            instance_info)
        if not proceed:
            return
    opers = gandi.paas.restart(resource, background)
    if background:
        for oper in opers:
            output_generic(gandi, oper, output_keys)
    return opers