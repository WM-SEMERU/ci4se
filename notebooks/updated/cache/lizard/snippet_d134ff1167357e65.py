def _create_parser(self):
    parser = CommandParser(get_internal_version_str())
    parser.register_list_command(self._setup_run_command(ListCommand))
    parser.register_upload_command(self._setup_run_command(UploadCommand))
    parser.register_add_user_command(self._setup_run_command(AddUserCommand))
    parser.register_remove_user_command(self._setup_run_command(
        RemoveUserCommand))
    parser.register_download_command(self._setup_run_command(DownloadCommand))
    parser.register_share_command(self._setup_run_command(ShareCommand))
    parser.register_deliver_command(self._setup_run_command(DeliverCommand))
    parser.register_delete_command(self._setup_run_command(DeleteCommand))
    parser.register_list_auth_roles_command(self._setup_run_command(
        ListAuthRolesCommand))
    return parser