def parse_groups(self, group, params):
    if group['GroupName'] in self.groups:
        return
    api_client = params['api_client']
    group['id'] = group.pop('GroupId')
    group['name'] = group.pop('GroupName')
    group['arn'] = group.pop('Arn')
    group['users'] = self.__fetch_group_users(api_client, group['name'])
    policies = self.__get_inline_policies(api_client, 'group', group['id'],
        group['name'])
    if len(policies):
        group['inline_policies'] = policies
    group['inline_policies_count'] = len(policies)
    self.groups[group['id']] = group