def create(self):
    out = helm('repo', 'add', 'jupyterhub', self.helm_repo)
    out = helm('repo', 'update')
    secret_yaml = self.get_security_yaml()
    out = helm('upgrade', '--install', self.release,
        'jupyterhub/jupyterhub', namespace=self.namespace, version=self.
        version, input=secret_yaml)
    if out.returncode != 0:
        print(out.stderr)
    else:
        print(out.stdout)