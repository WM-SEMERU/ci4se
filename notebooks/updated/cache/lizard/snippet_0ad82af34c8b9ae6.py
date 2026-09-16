async def _storeAppt(self, appt):
    await self._hivedict.set(appt.iden, appt.pack())