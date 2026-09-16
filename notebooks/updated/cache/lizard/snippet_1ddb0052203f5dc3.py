def create_in_team(self, team, params={}, **options):
    path = '/teams/%s/projects' % team
    return self.client.post(path, params, **options)