def round_to_float(number, precision):
    rounded = Decimal(str(floor((number + precision / 2) // precision))
        ) * Decimal(str(precision))
    return float(rounded)