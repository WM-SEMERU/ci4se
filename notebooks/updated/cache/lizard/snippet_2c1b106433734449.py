def P(Document, *fields, **kw):
    __always__ = kw.pop('__always__', set())
    projected = set()
    omitted = set()
    for field in fields:
        if field[0] in ('-', '!'):
            omitted.add(field[1:])
        elif field[0] == '+':
            projected.add(field[1:])
        else:
            projected.add(field)
    if not projected:
        names = set(getattr(Document, '__projection__', Document.__fields__
            ) or Document.__fields__)
        projected = {name for name in names - omitted}
    projected |= __always__
    if not projected:
        projected = {'_id'}
    return {unicode(traverse(Document, name, name)): True for name in projected
        }