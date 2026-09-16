def float2dec(ft, decimal_digits):
    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_UP
        places = decimal.Decimal(10) ** -decimal_digits
        return decimal.Decimal.from_float(float(ft)).quantize(places)