def check_stoplimit_prices(price, label):
    try:
        if not isfinite(price):
            raise BadOrderParameters(msg=
                'Attempted to place an order with a {} price of {}.'.format
                (label, price))
    except TypeError:
        raise BadOrderParameters(msg=
            'Attempted to place an order with a {} price of {}.'.format(
            label, type(price)))
    if price < 0:
        raise BadOrderParameters(msg=
            "Can't place a {} order with a negative price.".format(label))