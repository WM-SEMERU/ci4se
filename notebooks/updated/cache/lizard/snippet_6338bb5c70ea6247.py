def standardize_role(role):
    role = role.lower()
    if any(c in role for c in {'synthesis', 'give', 'yield', 'afford',
        'product', 'preparation of'}):
        return 'product'
    return role