def validate_instance_id(self, instid):
    if re.match('[\\w-]+$', instid) is not None:
        if len(instid) <= 63 and len(instid) >= 1:
            if instid[0].isalpha():
                return True
    return (
        '*** Error: Instance ids must be 1-63 alphanumeric characters,             first is a letter.'
        )