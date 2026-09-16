def post(url, var):
    data = {b[0]: b[1] for b in [a.split('=') for a in var]}
    writeln('Sending data to url', url)
    response = requests.post(url, data=data)
    if response.status_code == 200:
        writeln(response.text)
    else:
        writeln(str(response.status_code), response.reason)