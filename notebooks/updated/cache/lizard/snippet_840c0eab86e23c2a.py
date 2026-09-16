def ec2_credentials_list(user_id=None, name=None, profile=None, **
    connection_args):
    kstone = auth(profile, **connection_args)
    ret = {}
    if name:
        for user in kstone.users.list():
            if user.name == name:
                user_id = user.id
                break
    if not user_id:
        return {'Error': 'Unable to resolve user id'}
    for ec2_credential in kstone.ec2.list(user_id):
        ret[ec2_credential.user_id] = {'user_id': ec2_credential.user_id,
            'tenant_id': ec2_credential.tenant_id, 'access': ec2_credential
            .access, 'secret': ec2_credential.secret}
    return ret