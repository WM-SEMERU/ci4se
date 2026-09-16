def _parse_openssl_req(csr_filename):
    if not salt.utils.path.which('openssl'):
        raise salt.exceptions.SaltInvocationError(
            'openssl binary not found in path')
    cmd = 'openssl req -text -noout -in {0}'.format(csr_filename)
    output = __salt__['cmd.run_stdout'](cmd)
    output = re.sub(': rsaEncryption', ':', output)
    output = re.sub('[0-9a-f]{2}:', '', output)
    return salt.utils.data.decode(salt.utils.yaml.safe_load(output))