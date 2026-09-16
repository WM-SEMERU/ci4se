def user_parse(data):
    user = data.get('response', {}).get('user', {})
    yield 'id', user.get('id')
    yield 'email', user.get('contact', {}).get('email')
    yield 'first_name', user.get('firstName')
    yield 'last_name', user.get('lastName')
    city, country = user.get('homeCity', ', ').split(', ')
    yield 'city', city
    yield 'country', country