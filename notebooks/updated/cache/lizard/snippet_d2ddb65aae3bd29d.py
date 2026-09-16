def _add_project_filter_auth_role_arg(arg_parser):
    help_text = (
        'Filters project listing to just those projects with the specified role. '
        )
    help_text += 'See command list_auth_roles for AuthRole values.'
    arg_parser.add_argument('--auth-role', metavar='AuthRole', type=
        to_unicode, dest='auth_role', help=help_text, default=None)