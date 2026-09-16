def save(self, updateBy=None, *args, **kwargs):
    if (self.staffMember and self.staffMember.userAccount and not self.user or
        isinstance(updateBy, StaffMember) and self.staffMember.userAccount):
        self.user = self.staffMember.userAccount
    elif self.user and getattr(self.user, 'staffmember', None
        ) and not self.staffMember or isinstance(updateBy, User) and getattr(
        self.user, 'staffmember', None):
        self.staffMember = self.user.staffmember
    if not self.name:
        if self.user and self.user.get_full_name():
            self.name = self.user.get_full_name()
        elif self.staffMember:
            self.name = (self.staffMember.fullName or self.staffMember.
                privateEmail)
        elif self.location:
            self.name = self.location.name
    super(TransactionParty, self).save(*args, **kwargs)