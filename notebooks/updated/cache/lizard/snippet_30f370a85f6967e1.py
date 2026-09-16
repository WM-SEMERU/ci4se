def get_symbols(self, name):
    url = (
        'http://autoc.finance.yahoo.com/autoc?query={0}&callback=YAHOO.Finance.SymbolSuggest.ssCallback'
        .format(name))
    response = requests.get(url)
    json_data = re.match('YAHOO\\.Finance\\.SymbolSuggest.ssCallback\\((.*)\\)'
        , response.text)
    try:
        json_data = json_data.groups()[0]
    except (Exception,) as e:
        print(e)
        json_data = '{"results": "Webservice seems to be down"}'
    return type('response', (requests.Response,), {'text': json_data,
        'content': json_data.encode(), 'status_code': response.status_code,
        'reason': response.reason, 'encoding': response.encoding,
        'apparent_encoding': response.apparent_encoding, 'cookies':
        response.cookies, 'headers': response.headers, 'json': lambda :
        json.loads(json_data), 'url': response.url})