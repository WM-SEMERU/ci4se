def save_new_site(site_name, sitedir, srcdir, port, address, site_url,
    passwords):
    cp = ConfigParser.SafeConfigParser()
    cp.read([srcdir + '/.datacats-environment'])
    section_name = 'site_' + site_name
    if not cp.has_section(section_name):
        cp.add_section(section_name)
    cp.set(section_name, 'port', str(port))
    if address:
        cp.set(section_name, 'address', address)
    if site_url:
        cp.set(section_name, 'site_url', site_url)
    with open(srcdir + '/.datacats-environment', 'w') as config:
        cp.write(config)
    cp = ConfigParser.SafeConfigParser()
    cp.add_section('passwords')
    for n in sorted(passwords):
        cp.set('passwords', n.lower(), passwords[n])
    with open(sitedir + '/passwords.ini', 'w') as config:
        cp.write(config)