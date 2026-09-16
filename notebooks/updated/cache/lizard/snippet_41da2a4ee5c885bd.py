def change_by(cls, name, num):
    count = cls.count(name)
    if count + num < 0:
        raise CounterValueError('Counter[%s] will be negative after %+d.' %
            (name, num))
    counter = cls.collection.find_and_modify({'name': name}, {'$inc': {
        'seq': num}}, new=True, upsert=True)
    return counter['seq']