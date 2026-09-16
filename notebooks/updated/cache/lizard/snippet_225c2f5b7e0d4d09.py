def getVATAmount(self):
    try:
        vatamount = self.getTotalPrice() - Decimal(self.getPrice())
    except:
        vatamount = Decimal('0.00')
    return vatamount.quantize(Decimal('0.00'))