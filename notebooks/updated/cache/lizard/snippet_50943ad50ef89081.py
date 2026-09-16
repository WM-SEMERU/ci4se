def parse_price(price_string):
    return float(re.sub('[£,]', '', price_string))
    match = re.match('(?P<amount>-?£[\\d,]+(\\.\\d{2})?)', price_string)
    if not match:
        raise ValueError("Charge not in format '(-)£16,000(.00)' : {}".
            format(repr(price_string)))
    return float(re.sub('[£,]', '', match.group('amount')))