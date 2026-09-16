def detach(gandi, resource, background, force):
    if not force:
        proceed = click.confirm('Are you sure you want to detach ip %s?' %
            resource)
        if not proceed:
            return
    return gandi.ip.detach(resource, background, force)