def getSubtotal(self):
    if self.supplyorder_lineitems:
        return sum([(Decimal(obj['Quantity']) * Decimal(obj['Price'])) for
            obj in self.supplyorder_lineitems])
    return 0