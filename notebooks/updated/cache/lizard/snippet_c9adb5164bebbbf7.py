def add_batch(self, loans, batch_amount=None):
    assert batch_amount is None or batch_amount % 25 == 0, 'batch_amount must be a multiple of 25'
    assert type(loans
        ) is list, 'The loans property must be a list. (not {0})'.format(type
        (loans))
    for loan in loans:
        loan_id = loan
        amount = batch_amount
        if type(loan) is dict:
            assert 'loan_id' in loan, 'Each loan dict must have a loan_id value'
            assert batch_amount or 'invest_amount' in loan, 'Could not determine how much to invest in loan {0}'.format(
                loan['loan_id'])
            loan_id = loan['loan_id']
            if amount is None and 'invest_amount' in loan:
                amount = loan['invest_amount']
        assert amount is not None, 'Could not determine how much to invest in loan {0}'.format(
            loan_id)
        assert amount % 25 == 0, 'Amount to invest must be a multiple of 25 (loan_id: {0})'.format(
            loan_id)
        self.add(loan_id, amount)