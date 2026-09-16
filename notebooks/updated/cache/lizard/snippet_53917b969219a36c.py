def transactional_async(func, args, kwds, **options):
    options.setdefault('propagation', datastore_rpc.TransactionOptions.ALLOWED)
    if args or kwds:
        return transaction_async(lambda : func(*args, **kwds), **options)
    return transaction_async(func, **options)