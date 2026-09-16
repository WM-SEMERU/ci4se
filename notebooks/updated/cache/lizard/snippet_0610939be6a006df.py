def register_add_user_command(self, add_user_func):
    description = 'Gives user permission to access a remote project.'
    add_user_parser = self.subparsers.add_parser('add-user', description=
        description)
    add_project_name_or_id_arg(add_user_parser, help_text_suffix=
        'add a user to')
    user_or_email = add_user_parser.add_mutually_exclusive_group(required=True)
    add_user_arg(user_or_email)
    add_email_arg(user_or_email)
    _add_auth_role_arg(add_user_parser, default_permissions='project_admin')
    add_user_parser.set_defaults(func=add_user_func)