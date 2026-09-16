def get_leaders(self, limit=10):
    if limit is None:
        limit = 10
    soup = get_soup('leaders')
    table = soup.find('table')
    leaders_table = table.find_all('table')[1]
    listleaders = leaders_table.find_all('tr')[2:]
    listleaders.pop(10)
    for i, leader in enumerate(listleaders):
        if i == limit:
            return
        if not leader.text == '':
            item = leader.find_all('td')
            yield User(item[1].text, '', item[2].text, item[3].text)