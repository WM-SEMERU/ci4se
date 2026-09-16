def add_algorithm(self, parser):
    help = (
        'The HashAlgorithm that will be used to generate the signature (default: %(default)s).'
         % {'default': ca_settings.CA_DIGEST_ALGORITHM.name})
    parser.add_argument('--algorithm', metavar='{sha512,sha256,...}',
        default=ca_settings.CA_DIGEST_ALGORITHM, action=AlgorithmAction,
        help=help)