def validate(self, bigchain, current_transactions=[]):
    input_conditions = []
    if self.operation == Transaction.CREATE:
        duplicates = any(txn for txn in current_transactions if txn.id ==
            self.id)
        if bigchain.is_committed(self.id) or duplicates:
            raise DuplicateTransaction('transaction `{}` already exists'.
                format(self.id))
        if not self.inputs_valid(input_conditions):
            raise InvalidSignature('Transaction signature is invalid.')
    elif self.operation == Transaction.TRANSFER:
        self.validate_transfer_inputs(bigchain, current_transactions)
    return self