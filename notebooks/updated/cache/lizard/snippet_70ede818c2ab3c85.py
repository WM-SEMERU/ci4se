def is_empty(self):
    ps = self.p_lst
    if len(ps) > 1:
        return False
    if not ps:
        raise InvalidXmlError('p:txBody must have at least one a:p')
    if ps[0].text != '':
        return False
    return True