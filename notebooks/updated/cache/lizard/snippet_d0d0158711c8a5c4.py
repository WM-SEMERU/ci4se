def ips_with_roles(self, roles, env=None, match_all=False):

    def func():
        return [s['external_ip'] for s in self.servers_with_roles(roles,
            env, match_all)]
    return func