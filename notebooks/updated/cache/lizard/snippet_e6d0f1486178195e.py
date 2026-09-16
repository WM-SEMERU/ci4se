def from_dict(data, ctx):
    data = data.copy()
    if data.get('amount') is not None:
        data['amount'] = ctx.convert_decimal_number(data.get('amount'))
    return TransferFundsRejectTransaction(**data)