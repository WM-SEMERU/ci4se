def getTotalPrice(self):
    price = self.getPrice()
    vat = self.getVAT()
    price = price and price or 0
    vat = vat and vat or 0
    return float(price) + float(price) * float(vat) / 100