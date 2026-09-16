def get_mobile_number(mobile):
    blanks = [' ', '.', ',', '(', ')', '-']
    for b in blanks:
        mobile = mobile.replace(b, '')
    return mobile