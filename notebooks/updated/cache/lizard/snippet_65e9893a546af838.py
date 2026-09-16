def GenerateKeys(config, overwrite_keys=False):
    if not hasattr(key_utils, 'MakeCACert'):
        raise OpenSourceKeyUtilsRequiredError(
            'Generate keys can only run with open source key_utils.')
    if config.Get('PrivateKeys.server_key', default=None
        ) and not overwrite_keys:
        print(config.Get('PrivateKeys.server_key'))
        raise KeysAlreadyExistError(
            'Config %s already has keys, use --overwrite_keys to override.' %
            config.parser)
    length = grr_config.CONFIG['Server.rsa_key_length']
    print('All keys will have a bit length of %d.' % length)
    print('Generating executable signing key')
    executable_key = rdf_crypto.RSAPrivateKey.GenerateKey(bits=length)
    config.Set('PrivateKeys.executable_signing_private_key', executable_key
        .AsPEM())
    config.Set('Client.executable_signing_public_key', executable_key.
        GetPublicKey().AsPEM())
    print('Generating CA keys')
    ca_key = rdf_crypto.RSAPrivateKey.GenerateKey(bits=length)
    ca_cert = key_utils.MakeCACert(ca_key)
    config.Set('CA.certificate', ca_cert.AsPEM())
    config.Set('PrivateKeys.ca_key', ca_key.AsPEM())
    print('Generating Server keys')
    server_key = rdf_crypto.RSAPrivateKey.GenerateKey(bits=length)
    server_cert = key_utils.MakeCASignedCert('grr', server_key, ca_cert, ca_key
        )
    config.Set('Frontend.certificate', server_cert.AsPEM())
    config.Set('PrivateKeys.server_key', server_key.AsPEM())
    print('Generating secret key for csrf protection.')
    _GenerateCSRFKey(config)