def parse_create(prs, conn):
    prs_create = prs.add_parser('create', help='create record of specific zone'
        )
    set_option(prs_create, 'domain')
    conn_options(prs_create, conn)
    prs_create.set_defaults(func=create)