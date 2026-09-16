def moveOrder(self, orderNumber, rate, amount=None, postOnly=None,
    immediateOrCancel=None):
    return self._private('moveOrder', orderNumber=orderNumber, rate=rate,
        amount=amount, postOnly=postOnly, immediateOrCancel=immediateOrCancel)