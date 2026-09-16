def get_currency_symbol(self):
    locale = locales.getLocale('en')
    setup = api.get_setup()
    currency = setup.getCurrency()
    return locale.numbers.currencies[currency].symbol