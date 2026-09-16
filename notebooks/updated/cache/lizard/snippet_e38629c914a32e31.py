def get_money_with_currency_format(self, amount):
    return self.money_formats[self.get_money_currency()][
        'money_with_currency_format'].format(amount=amount)