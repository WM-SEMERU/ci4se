def get_rate(currency):
    source = get_rate_source()
    try:
        return Rate.objects.get(source=source, currency=currency).value
    except Rate.DoesNotExist:
        raise CurrencyConversionException(
            'Rate for %s in %s do not exists. Please run python manage.py update_rates'
             % (currency, source.name))