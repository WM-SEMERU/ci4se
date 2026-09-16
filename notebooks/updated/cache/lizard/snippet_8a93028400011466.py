def move(self, fromaccount, toaccount, amount, minconf=1):
    amount = Decimal(amount).quantize(self.quantum, rounding=ROUND_HALF_EVEN)
    return self.rpc.call('move', fromaccount, toaccount, float(str(amount)),
        minconf)