def get_user_invitation_by_id(self, id):
    return self.db_adapter.get_object(self.UserInvitationClass, id=id)