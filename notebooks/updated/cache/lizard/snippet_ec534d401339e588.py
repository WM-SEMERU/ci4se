def create_transaction(self, to_account):
    from_account = self.statement_import.bank_account
    transaction = Transaction.objects.create()
    Leg.objects.create(transaction=transaction, account=from_account,
        amount=+(self.amount * -1))
    Leg.objects.create(transaction=transaction, account=to_account, amount=
        -(self.amount * -1))
    transaction.date = self.date
    transaction.save()
    self.transaction = transaction
    self.save()
    return transaction