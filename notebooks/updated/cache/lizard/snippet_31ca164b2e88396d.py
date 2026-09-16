def remove_signup(self, user=None, force=False, dont_run_waitlist=False):
    exception = eighth_exceptions.SignupException()
    if user is not None:
        if user != self.user and not user.is_eighth_admin:
            exception.SignupForbidden = True
    if self.scheduled_activity.block.locked:
        exception.BlockLocked = True
    if self.scheduled_activity.cancelled:
        exception.ScheduledActivityCancelled = True
    if self.scheduled_activity.activity.deleted:
        exception.ActivityDeleted = True
    if (self.scheduled_activity.activity and self.scheduled_activity.
        activity.sticky):
        exception.Sticky = True
    if len(exception.messages()) > 0 and not force:
        raise exception
    else:
        block = self.scheduled_activity.block
        self.delete()
        if settings.ENABLE_WAITLIST and self.scheduled_activity.waitlist.all(
            ).exists() and not block.locked and not dont_run_waitlist:
            if not self.scheduled_activity.is_full():
                waitlists = EighthWaitlist.objects.get_next_waitlist(self.
                    scheduled_activity)
                self.scheduled_activity.notify_waitlist(waitlists, self.
                    scheduled_activity)
        return 'Successfully removed signup for {}.'.format(block)