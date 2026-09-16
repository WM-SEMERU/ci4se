def account_balance_before(self):
    transaction_date = self.transaction.date
    return self.account.balance(leg_query=models.Q(transaction__date__lt=
        transaction_date) | models.Q(transaction__date=transaction_date) &
        models.Q(transaction_id__lt=self.transaction_id))