def update(self, client):
    update_cmd = "{sudo} '{refresh};{update}'".format(sudo=self.
        get_sudo_exec_wrapper(), refresh=self.get_refresh_repo_cmd(),
        update=self.get_update_cmd())
    out = ''
    try:
        out = ipa_utils.execute_ssh_command(client, update_cmd)
    except Exception as error:
        raise IpaDistroException('An error occurred updating instance: %s' %
            error)
    return out