def from_dict(data, ctx):
    data = data.copy()
    if data.get('baseBid') is not None:
        data['baseBid'] = ctx.convert_decimal_number(data.get('baseBid'))
    if data.get('baseAsk') is not None:
        data['baseAsk'] = ctx.convert_decimal_number(data.get('baseAsk'))
    if data.get('bids') is not None:
        data['bids'] = [ctx.pricing_common.PriceBucket.from_dict(d, ctx) for
            d in data.get('bids')]
    if data.get('asks') is not None:
        data['asks'] = [ctx.pricing_common.PriceBucket.from_dict(d, ctx) for
            d in data.get('asks')]
    if data.get('closeoutBid') is not None:
        data['closeoutBid'] = ctx.convert_decimal_number(data.get(
            'closeoutBid'))
    if data.get('closeoutAsk') is not None:
        data['closeoutAsk'] = ctx.convert_decimal_number(data.get(
            'closeoutAsk'))
    return Price(**data)