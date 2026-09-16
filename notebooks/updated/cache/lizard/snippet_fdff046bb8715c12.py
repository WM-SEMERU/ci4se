def do_start_role(self, role):
    if not role:
        return None
    if not self.has_cluster():
        return None
    if '-' not in role:
        print('Please enter a valid role name')
        return None
    try:
        service = api.get_cluster(self.cluster).get_service(role.split('-')[0])
        service.start_roles(role)
        print('Starting Role')
    except ApiException:
        print('Error: Role or Service Not Found')