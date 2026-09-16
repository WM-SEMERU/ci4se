def get_uid(self, context, value):
    if not value or value == ['']:
        ret = ''
    elif api.is_brain(value):
        ret = value.UID
    elif api.is_at_content(value) or api.is_dexterity_content(value):
        ret = value.UID()
    elif api.is_uid(value):
        ret = value
    else:
        raise ReferenceException('{}.{}: Cannot resolve UID for {}'.format(
            context, self.getName(), value))
    return ret