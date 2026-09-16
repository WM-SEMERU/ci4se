def get_gnupg_components(sp=subprocess):
    args = [util.which('gpgconf'), '--list-components']
    output = check_output(args=args, sp=sp)
    components = dict(re.findall('(.*):.*:(.*)', output.decode('utf-8')))
    log.debug('gpgconf --list-components: %s', components)
    return components