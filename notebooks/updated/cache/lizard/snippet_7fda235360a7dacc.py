def _validate_bag(self, bag, **kwargs):
    failed = None
    try:
        bag.validate(**kwargs)
    except BagValidationError as e:
        failed = e
    if failed:
        raise BagValidationError('%s' % failed)