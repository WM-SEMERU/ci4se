def sequence(context, data):
    number = data.get('number', context.params.get('start', 1))
    stop = context.params.get('stop')
    step = context.params.get('step', 1)
    delay = context.params.get('delay')
    prefix = context.params.get('tag')
    while True:
        tag = None if prefix is None else '%s:%s' % (prefix, number)
        if tag is None or not context.check_tag(tag):
            context.emit(data={'number': number})
        if tag is not None:
            context.set_tag(tag, True)
        number = number + step
        if step > 0 and number >= stop:
            break
        if step < 0 and number <= stop:
            break
        if delay is not None:
            context.recurse(data={'number': number}, delay=delay)
            break