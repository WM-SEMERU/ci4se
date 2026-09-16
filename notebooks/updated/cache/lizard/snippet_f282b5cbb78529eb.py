def get_next_type(self):
    import sys
    from ..osid.osid_errors import IllegalState, OperationFailed
    try:
        next_item = self.next()
    except StopIteration:
        raise IllegalState('no more elements available in this list')
    except:
        raise OperationFailed()
    else:
        return next_item