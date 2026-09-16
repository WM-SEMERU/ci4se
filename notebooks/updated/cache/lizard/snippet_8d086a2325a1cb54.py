def CheckUserForLabels(username, authorized_labels, token=None):
    authorized_labels = set(authorized_labels)
    try:
        user = aff4.FACTORY.Open('aff4:/users/%s' % username, aff4_type=
            aff4_users.GRRUser, token=token)
        if authorized_labels.intersection(user.GetLabelsNames()
            ) == authorized_labels:
            return True
        else:
            raise access_control.UnauthorizedAccess(
                'User %s is missing labels (required: %s).' % (username,
                authorized_labels))
    except IOError:
        raise access_control.UnauthorizedAccess('User %s not found.' % username
            )