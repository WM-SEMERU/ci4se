def parse_update_soa(prs, conn):
    prs_soa = prs.add_parser('soa', help='update SOA record')
    prs_soa.add_argument('--domain', action='store', required=True, help=
        'specify domain FQDN')
    prs_soa.add_argument('--mname', action='store', help=
        'specify MNAME of SOA record')
    prs_soa.add_argument('--rname', action='store', help=
        'specify RNAME of SOA record')
    prs_soa.add_argument('--refresh', action='store', type=int, help=
        'specify REFRESH of SOA record')
    prs_soa.add_argument('--retry', action='store', type=int, help=
        'specify RETRY of SOA record')
    prs_soa.add_argument('--expire', action='store', type=int, help=
        'specify EXPIRE of SOA record')
    prs_soa.add_argument('--minimum', action='store', type=int, help=
        'specify MINIMUM of SOA record')
    conn_options(prs_soa, conn)
    prs_soa.set_defaults(func=update_soa_serial)