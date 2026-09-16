def absence_info(self):
    from ..eighth.models import EighthSignup
    return EighthSignup.objects.filter(user=self, was_absent=True,
        scheduled_activity__attendance_taken=True)