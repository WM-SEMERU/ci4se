def transacted(func):

    def transactionified(item, *a, **kw):
        return item.store.transact(func, item, *a, **kw)
    return mergeFunctionMetadata(func, transactionified)