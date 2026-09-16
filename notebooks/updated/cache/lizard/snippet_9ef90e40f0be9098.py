def callCount(cls, spy, number):
    cls.__is_spy(spy)
    if not spy.callCount == number:
        raise cls.failException(cls.message)