def run(self, args):
    email = args.email
    username = args.username
    copy_project = args.copy_project
    force_send = args.resend
    msg_file = args.msg_file
    share_usernames = args.share_usernames
    share_emails = args.share_emails
    message = read_argument_file_contents(msg_file)
    project = self.fetch_project(args, must_exist=True, include_children=False)
    share_users = self.make_user_list(share_emails, share_usernames)
    print('Delivering project.')
    new_project_name = None
    if copy_project:
        new_project_name = self.get_new_project_name(project.name)
    to_user = self.remote_store.lookup_or_register_user_by_email_or_username(
        email, username)
    try:
        path_filter = PathFilter(args.include_paths, args.exclude_paths)
        dest_email = self.service.deliver(project, new_project_name,
            to_user, share_users, force_send, path_filter, message)
        print('Delivery email message sent to ' + dest_email)
    except D4S2Error as ex:
        if ex.warning:
            print(ex.message)
        else:
            raise