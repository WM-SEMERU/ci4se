def gen_ca_cert(filename, dirname, days, silent=False):
    keyfile = os.path.join(dirname, '{}.key'.format(filename))
    ca_crt = os.path.join(dirname, '{}.crt'.format(filename))
    gen_private_key(keyfile, silent)
    gen_self_signed_cert(ca_crt, keyfile, days, silent)