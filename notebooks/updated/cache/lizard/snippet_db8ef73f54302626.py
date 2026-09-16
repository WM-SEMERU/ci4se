def extend_identity(identity, groups):
    provides = set([UserNeed(current_user.email)] + [RoleNeed('{0}@cern.ch'
        .format(name)) for name in groups])
    identity.provides |= provides
    session[OAUTHCLIENT_CERN_SESSION_KEY] = provides