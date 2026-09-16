def delete_ace(self, domain=None, user=None, sid=None):
    if sid is None:
        if domain is None:
            domain = self.cifs_server.domain
        sid = UnityAclUser.get_sid(self._cli, user=user, domain=domain)
    if isinstance(sid, six.string_types):
        sid = [sid]
    ace_list = [self._make_remove_ace_entry(s) for s in sid]
    resp = self.action('setACEs', cifsShareACEs=ace_list)
    resp.raise_if_err()
    return resp