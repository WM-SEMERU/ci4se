def sign_filter_permissions(permissions):
    permissions = {key.lower(): value for key, value in permissions.iteritems()
        }
    return signing.dumps(permissions, compress=True)