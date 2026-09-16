def load_permissions_on_identity_loaded(sender, identity):
    identity.provides.add(any_user)
    if current_user.is_authenticated:
        identity.provides.add(authenticated_user)