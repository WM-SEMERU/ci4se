def get_joke():
    page = requests.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
    if page.status_code == 200:
        jokes = []
        jokes = json.loads(page.content.decode(page.encoding))
        return '"' + jokes[0] + '" - Ron Swanson'
    return None