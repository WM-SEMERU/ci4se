def get_referenced_object(self):
    if self._BunqMeFundraiserResult is not None:
        return self._BunqMeFundraiserResult
    if self._BunqMeTab is not None:
        return self._BunqMeTab
    if self._BunqMeTabResultInquiry is not None:
        return self._BunqMeTabResultInquiry
    if self._BunqMeTabResultResponse is not None:
        return self._BunqMeTabResultResponse
    if self._ChatMessage is not None:
        return self._ChatMessage
    if self._DraftPayment is not None:
        return self._DraftPayment
    if self._IdealMerchantTransaction is not None:
        return self._IdealMerchantTransaction
    if self._Invoice is not None:
        return self._Invoice
    if self._MasterCardAction is not None:
        return self._MasterCardAction
    if self._MonetaryAccount is not None:
        return self._MonetaryAccount
    if self._Payment is not None:
        return self._Payment
    if self._PaymentBatch is not None:
        return self._PaymentBatch
    if self._RequestInquiry is not None:
        return self._RequestInquiry
    if self._RequestInquiryBatch is not None:
        return self._RequestInquiryBatch
    if self._RequestResponse is not None:
        return self._RequestResponse
    if self._ShareInviteBankInquiry is not None:
        return self._ShareInviteBankInquiry
    if self._ShareInviteBankResponse is not None:
        return self._ShareInviteBankResponse
    if self._ScheduledPayment is not None:
        return self._ScheduledPayment
    if self._ScheduledInstance is not None:
        return self._ScheduledInstance
    if self._TabResultInquiry is not None:
        return self._TabResultInquiry
    if self._TabResultResponse is not None:
        return self._TabResultResponse
    if self._User is not None:
        return self._User
    raise exception.BunqException(self._ERROR_NULL_FIELDS)