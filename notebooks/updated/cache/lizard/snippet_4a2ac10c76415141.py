def has_membership(self, user, role):
    targetRecord = AuthMembership.objects(creator=self.client, user=user
        ).first()
    if targetRecord:
        return role in [i.role for i in targetRecord.groups]
    return False