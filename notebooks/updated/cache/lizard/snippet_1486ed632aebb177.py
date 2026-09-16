def DeleteGRRUser(self, username):
    try:
        del self.approvals_by_username[username]
    except KeyError:
        pass
    for approvals in itervalues(self.approvals_by_username):
        for approval in itervalues(approvals):
            grants = [g for g in approval.grants if g.grantor_username !=
                username]
            if len(grants) != len(approval.grants):
                approval.grants = grants
    try:
        del self.notifications_by_username[username]
    except KeyError:
        pass
    try:
        del self.users[username]
    except KeyError:
        raise db.UnknownGRRUserError(username)