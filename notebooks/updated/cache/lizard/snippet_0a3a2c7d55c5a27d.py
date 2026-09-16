def guessFormat(self, name):
    name = name.lower()
    generator = self.generator
    if re.findall('^is[_A-Z]', name):
        return lambda x: generator.boolean()
    if re.findall('(_a|A)t$', name):
        return lambda x: generator.dateTime()
    if name in ('first_name', 'firstname'):
        return lambda x: generator.firstName()
    if name in ('last_name', 'lastname'):
        return lambda x: generator.lastName()
    if name in ('username', 'login', 'nickname'):
        return lambda x: generator.userName()
    if name in ('email', 'email_address'):
        return lambda x: generator.email()
    if name in ('phone_number', 'phonenumber', 'phone'):
        return lambda x: generator.phoneNumber()
    if name == 'address':
        return lambda x: generator.address()
    if name == 'city':
        return lambda x: generator.city()
    if name == 'streetaddress':
        return lambda x: generator.streetaddress()
    if name in ('postcode', 'zipcode'):
        return lambda x: generator.postcode()
    if name == 'state':
        return lambda x: generator.state()
    if name == 'country':
        return lambda x: generator.country()
    if name == 'title':
        return lambda x: generator.sentence()
    if name in ('body', 'summary', 'description'):
        return lambda x: generator.text()