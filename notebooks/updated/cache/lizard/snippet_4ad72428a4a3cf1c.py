def is_all_field_none(self):
    if self._BillingInvoice is not None:
        return False
    if self._DraftPayment is not None:
        return False
    if self._MasterCardAction is not None:
        return False
    if self._Payment is not None:
        return False
    if self._PaymentBatch is not None:
        return False
    if self._RequestResponse is not None:
        return False
    if self._ScheduleInstance is not None:
        return False
    if self._TabResultResponse is not None:
        return False
    if self._WhitelistResult is not None:
        return False
    return True