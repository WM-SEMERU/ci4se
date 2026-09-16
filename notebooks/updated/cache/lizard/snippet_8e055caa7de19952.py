def to_xdr_object(self):
    source_account = account_xdr_object(self.source)
    memo = self.memo.to_xdr_object()
    operations = [o.to_xdr_object() for o in self.operations]
    ext = Xdr.nullclass()
    ext.v = 0
    return Xdr.types.Transaction(source_account, self.fee, self.sequence,
        self.time_bounds, memo, operations, ext)