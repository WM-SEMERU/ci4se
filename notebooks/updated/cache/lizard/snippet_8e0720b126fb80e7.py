def create_address(customer_id, data):
    Address = client.model('party.address')
    Country = client.model('country.country')
    Subdivision = client.model('country.subdivision')
    country, = Country.find([('code', '=', data['country'])])
    state, = Subdivision.find([('code', 'ilike', '%-' + data['state']), (
        'country', '=', country['id'])])
    address, = Address.create([{'party': customer_id, 'name': data['name'],
        'street': data['street'], 'street_bis': data['street_bis'], 'city':
        data['city'], 'zip': data['zip'], 'country': country['id'],
        'subdivision': state['id']}])
    return address['id']