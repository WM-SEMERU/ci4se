def get_next_activity(self):
    try:
        next_object = next(self)
    except StopIteration:
        raise IllegalState('no more elements available in this list')
    except Exception:
        raise OperationFailed()
    else:
        return next_object