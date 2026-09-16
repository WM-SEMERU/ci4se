def extract_public_key(args):
    sk = _load_ecdsa_signing_key(args)
    vk = sk.get_verifying_key()
    args.public_keyfile.write(vk.to_string())
    print('%s public key extracted to %s' % (args.keyfile.name, args.
        public_keyfile.name))