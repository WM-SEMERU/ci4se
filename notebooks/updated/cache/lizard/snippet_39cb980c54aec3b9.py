def eval_bool(self, expr):
    result = expr.eval(self)
    iterator = iter(result)
    try:
        next(iterator)
    except StopIteration:
        return False
    else:
        return True
    finally:
        if hasattr(iterator, 'close'):
            iterator.close()