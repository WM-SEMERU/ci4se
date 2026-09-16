def _is_valid_date_time(self, inpt, metadata):
    from dlkit.abstract_osid.calendaring.primitives import DateTime as abc_datetime
    if isinstance(inpt, abc_datetime):
        return True
    else:
        return False