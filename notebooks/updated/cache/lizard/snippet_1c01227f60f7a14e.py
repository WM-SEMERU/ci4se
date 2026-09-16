def isSelfVerificationEnabled(self):
    bsve = self.bika_setup.getSelfVerificationEnabled()
    vs = self.getSelfVerification()
    return bsve if vs == -1 else vs == 1