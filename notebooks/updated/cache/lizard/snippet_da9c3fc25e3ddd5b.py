def create_contact(self, email=None, first_name=None, last_name=None,
    phone_number=None):
    result = {}
    if email:
        result['email'] = email
    if first_name is not None:
        result['first_name'] = first_name
    if last_name is not None:
        result['last_name'] = last_name
    if phone_number is not None:
        result['phone_number'] = phone_number
    return result if len(result) > 0 else None