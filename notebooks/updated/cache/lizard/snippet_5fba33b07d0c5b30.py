def keys_delete(gandi, fqdn, key, force):
    if not force:
        proceed = click.confirm(
            'Are you sure you want to delete key %s on domain %s?' % (key,
            fqdn))
        if not proceed:
            return
    result = gandi.dns.keys_delete(fqdn, key)
    gandi.echo('Delete successful.')
    return result