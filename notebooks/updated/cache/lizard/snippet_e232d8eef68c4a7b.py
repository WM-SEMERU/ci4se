def install_ca_cert(ca_cert, name=None):
    if not ca_cert:
        return
    if not isinstance(ca_cert, bytes):
        ca_cert = ca_cert.encode('utf8')
    if not name:
        name = 'juju-{}'.format(charm_name())
    cert_file = '/usr/local/share/ca-certificates/{}.crt'.format(name)
    new_hash = hashlib.md5(ca_cert).hexdigest()
    if file_hash(cert_file) == new_hash:
        return
    log('Installing new CA cert at: {}'.format(cert_file), level=INFO)
    write_file(cert_file, ca_cert)
    subprocess.check_call(['update-ca-certificates', '--fresh'])