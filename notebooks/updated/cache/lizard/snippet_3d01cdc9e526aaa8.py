def delete(gandi, fqdn, name, type, force):
    domains = gandi.dns.list()
    domains = [domain['fqdn'] for domain in domains]
    if fqdn not in domains:
        gandi.echo('Sorry domain %s does not exist' % fqdn)
        gandi.echo('Please use one of the following: %s' % ', '.join(domains))
        return
    if not force:
        if not name and not type:
            prompt = ('Are you sure to delete all records for domain %s ?' %
                fqdn)
        elif name and not type:
            prompt = (
                "Are you sure to delete all '%s' name records for domain %s ?"
                 % (name, fqdn))
        else:
            prompt = (
                "Are you sure to delete all '%s' records of type %s for domain %s ?"
                 % (name, type, fqdn))
        proceed = click.confirm(prompt)
        if not proceed:
            return
    result = gandi.dns.del_record(fqdn, name, type)
    gandi.echo('Delete successful.')
    return result