def Approval(self, username, approval_id):
    return HuntApprovalRef(hunt_id=self.hunt_id, username=username,
        approval_id=approval_id, context=self._context)