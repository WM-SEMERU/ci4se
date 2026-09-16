def CountDictCall(keyfunc):

    def decorator(fn):
        if use_memoizer:

            def wrapper(self, *args, **kwargs):
                global CounterList
                key = self.__class__.__name__ + '.' + fn.__name__
                if key not in CounterList:
                    CounterList[key] = CountDict(self.__class__.__name__,
                        fn.__name__, keyfunc)
                CounterList[key].count(self, *args, **kwargs)
                return fn(self, *args, **kwargs)
            wrapper.__name__ = fn.__name__
            return wrapper
        else:
            return fn
    return decorator