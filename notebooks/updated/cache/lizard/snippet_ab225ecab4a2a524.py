def deleteldapgrouplink(self, group_id, cn, provider=None):
    url = '{base}/{gid}/ldap_group_links/{provider}{cn}'.format(base=self.
        groups_url, gid=group_id, cn=cn, provider='{0}/'.format(provider) if
        provider else '')
    request = requests.delete(url, headers=self.headers, verify=self.verify_ssl
        )
    return request.status_code == 200