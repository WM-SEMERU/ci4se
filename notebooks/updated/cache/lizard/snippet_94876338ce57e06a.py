def subcmd_relist_parser(subcmd):
    subcmd.add_argument('--broker-name', action='store', dest='broker_name',
        help='Name of the ServiceBroker k8s resource', default=
        'ansible-service-broker')
    subcmd.add_argument('--secure', action='store_true', dest='verify',
        help='Verify SSL connection to Ansible Service Broker', default=False)
    subcmd.add_argument('--ca-path', action='store', dest='cert', help=
        'CA cert to use for verifying SSL connection to Ansible Service Broker'
        , default=None)
    subcmd.add_argument('--username', '-u', action='store', default=None,
        dest='basic_auth_username', help=
        'Specify the basic auth username to be used')
    subcmd.add_argument('--password', '-p', action='store', default=None,
        dest='basic_auth_password', help=
        'Specify the basic auth password to be used')
    return