def from_dict(data, ctx):
    data = data.copy()
    if data.get('price') is not None:
        data['price'] = ctx.convert_decimal_number(data.get('price'))
    if data.get('bucketWidth') is not None:
        data['bucketWidth'] = ctx.convert_decimal_number(data.get(
            'bucketWidth'))
    if data.get('buckets') is not None:
        data['buckets'] = [ctx.instrument.OrderBookBucket.from_dict(d, ctx) for
            d in data.get('buckets')]
    return OrderBook(**data)