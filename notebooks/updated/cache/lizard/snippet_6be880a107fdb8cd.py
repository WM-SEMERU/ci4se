def query_cast(value, answers, ignorecase=False):
    if ignorecase:
        value = value.lower()
    for item in answers:
        for a in item['values']:
            if ignorecase and value == str(a).lower():
                return item['values'][0]
            elif value == a:
                return item['values'][0]
    raise ValueError("Response '%s' not understood, please try again." % value)