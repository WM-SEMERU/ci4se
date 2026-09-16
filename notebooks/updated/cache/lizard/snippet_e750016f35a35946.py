def separate(self):
    collections = []
    start = None
    end = None
    for index in self.indexes:
        if start is None:
            start = index
            end = start
            continue
        if index != end + 1:
            collections.append(Collection(self.head, self.tail, self.
                padding, indexes=set(range(start, end + 1))))
            start = index
        end = index
    if start is None:
        collections.append(Collection(self.head, self.tail, self.padding))
    else:
        collections.append(Collection(self.head, self.tail, self.padding,
            indexes=range(start, end + 1)))
    return collections