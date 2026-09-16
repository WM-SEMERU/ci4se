def remove_domain_user_role(request, user, role, domain=None):
    manager = keystoneclient(request, admin=True).roles
    return manager.revoke(role, user=user, domain=domain)