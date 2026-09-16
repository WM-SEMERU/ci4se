def validate_number(self, number):
    if not isinstance(number, str):
        raise ElksException('Recipient phone number may not be empty')
    if number[0] == '+' and len(number) > 2 and len(number) < 16:
        return True
    else:
        raise ElksException('Phone number must be of format +CCCXXX...')