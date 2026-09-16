def each_do(action: Callable[[T], None]):

    def inner(collection: ActualIterable[T]):
        for each in collection:
            action(each)
    return inner