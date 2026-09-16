def checkIfAvailable(self, dateTime=timezone.now()):
    return self.startTime >= dateTime + timedelta(days=getConstant(
        'privateLessons__closeBookingDays')
        ) and self.startTime <= dateTime + timedelta(days=getConstant(
        'privateLessons__openBookingDays')
        ) and not self.eventRegistration and (self.status == self.
        SlotStatus.available or self.status == self.SlotStatus.tentative and
        getattr(getattr(self.temporaryEventRegistration, 'registration',
        None), 'expirationDate', timezone.now()) <= timezone.now())