def assign_yourself(self):
    task_invitation = TaskInvitation.objects.get(self.task_invitation_key)
    wfi = task_invitation.instance
    if not wfi.current_actor.exist:
        wfi.current_actor = self.current.role
        wfi.save()
        [inv.delete() for inv in TaskInvitation.objects.filter(instance=wfi
            ) if not inv == task_invitation]
        title = _('Successful')
        msg = _('You have successfully assigned the job to yourself.')
    else:
        title = _('Unsuccessful')
        msg = _('Unfortunately, this job is already taken by someone else.')
    self.current.msg_box(title=title, msg=msg)