def loader():
    url = request.args.get('url')
    response = requests.get(url)
    return response.content