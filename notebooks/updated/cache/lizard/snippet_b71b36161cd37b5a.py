def _handle_ssh_callback(self, submission_id, host, port, password):
    if host is not None:
        obj = {'ssh_host': host, 'ssh_port': port, 'ssh_password': password}
        self._database.submissions.update_one({'_id': submission_id}, {
            '$set': obj})