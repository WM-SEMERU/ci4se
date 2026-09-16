def sign(self, user_visible_data, personal_number=None, **kwargs):
    if 'requirementAlternatives' in kwargs:
        warnings.warn('Requirement Alternatives option is not tested.',
            BankIDWarning)
    if isinstance(user_visible_data, six.text_type):
        data = base64.b64encode(user_visible_data.encode('utf-8')).decode(
            'ascii')
    else:
        data = base64.b64encode(user_visible_data).decode('ascii')
    try:
        out = self.client.service.Sign(userVisibleData=data, personalNumber
            =personal_number, **kwargs)
    except Error as e:
        raise get_error_class(e, 'Could not complete Sign order.')
    return self._dictify(out)