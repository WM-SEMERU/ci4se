def deskew(self, reduction_factor=0):
    with _LeptonicaErrorTrap():
        return Pix(lept.pixDeskew(self._cdata, reduction_factor))