def create(gandi, fqdn, name, type, value, ttl):
    domains = gandi.dns.list()
    domains = [domain['fqdn'] for domain in domains]
    if fqdn not in domains:
        gandi.echo('Sorry domain %s does not exist' % fqdn)
        gandi.echo('Please use one of the following: %s' % ', '.join(domains))
        return
    result = gandi.dns.add_record(fqdn, name, type, value, ttl)
    gandi.echo(result['message'])