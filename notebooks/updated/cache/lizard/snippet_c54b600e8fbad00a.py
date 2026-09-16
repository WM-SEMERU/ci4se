def get_currency(currency_str):
    path = 'units/currencies.csv'
    filepath = pkg_resources.resource_filename('mpu', path)
    with open(filepath, 'r') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        next(reader, None)
        for row in reader:
            is_currency = currency_str in [row[0], row[1], row[2]]
            if is_currency:
                entity = row[0]
                name = row[1]
                code = row[2]
                numeric_code = row[3]
                symbol = row[4]
                if len(row[5]) == 0:
                    exponent = None
                else:
                    exponent = int(row[5])
                if len(row[6]) > 0:
                    withdrawal_date = row[6]
                else:
                    withdrawal_date = None
                subunits = row[7]
                return Currency(name=name, code=code, numeric_code=
                    numeric_code, symbol=symbol, exponent=exponent,
                    entities=[entity], withdrawal_date=withdrawal_date,
                    subunits=subunits)
    raise ValueError("Could not find currency '{}'".format(currency_str))