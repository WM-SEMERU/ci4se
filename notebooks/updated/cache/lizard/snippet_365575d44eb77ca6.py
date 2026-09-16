def query(botcust2, message):
    logger.debug('Getting Mitsuku reply')
    params = {'botid': 'f6a012073e345a08', 'amp;skin': 'chat'}
    headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language':
        'en-US,en;q=0.8', 'Cache-Control': 'max-age=0', 'Connection':
        'keep-alive', 'Content-Length': str(len(message) + 34),
        'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 
        'botcust2=' + botcust2, 'DNT': '1', 'Host': 'kakko.pandorabots.com',
        'Origin': 'https://kakko.pandorabots.com', 'Referer':
        'https://kakko.pandorabots.com/pandora/talk?botid=f6a012073e345a08&amp;skin=chat'
        , 'Upgrade-Insecure-Requests': '1', 'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    data = {'botcust2': botcust2, 'message': message}
    logger.debug('Sending POST request')
    response = requests.post(url, params=params, headers=headers, data=data)
    logger.debug('POST response {}'.format(response))
    parsed = lxml.html.parse(io.StringIO(response.text)).getroot()
    try:
        result = parsed[1][2][0][2].tail[1:]
        logger.debug('Getting botcust2 successful')
    except IndexError:
        result = False
        logger.critical('Getting botcust2 from html failed')
    return result