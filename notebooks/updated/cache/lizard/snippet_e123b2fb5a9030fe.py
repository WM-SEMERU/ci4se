def generate(fn):
    if isinstance(fn, str):
        return lambda f: generate(f).desc(fn)

    @wraps(fn)
    @Parser
    def generated(text, index):
        iterator, value = fn(), None
        try:
            while True:
                parser = iterator.send(value)
                res = parser(text, index)
                if not res.status:
                    return res
                value, index = res.value, res.index
        except StopIteration as stop:
            endval = stop.value
            if isinstance(endval, Parser):
                return endval(text, index)
            else:
                return Value.success(index, endval)
    return generated.desc(fn.__name__)