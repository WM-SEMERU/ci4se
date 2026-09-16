def to_string(cls, error_code):
    if error_code == cls.ILLEGAL_COMMAND:
        return 'Failed to erase sector.'
    return super(JLinkEraseErrors, cls).to_string(error_code)