def do_create(marfile, files, compress, productversion=None, channel=None,
    signing_key=None, signing_algorithm=None):
    with open(marfile, 'w+b') as f:
        with MarWriter(f, productversion=productversion, channel=channel,
            signing_key=signing_key, signing_algorithm=signing_algorithm) as m:
            for f in files:
                m.add(f, compress=compress)