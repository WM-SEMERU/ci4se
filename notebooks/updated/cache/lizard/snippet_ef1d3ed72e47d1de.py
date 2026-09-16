def query_rpdns(self):
    results = requests.get('https://freeapi.robtex.com/pdns/reverse/{}'.
        format(self.get_data())).text.split('\r\n')
    jsonresults = []
    for idx, r in enumerate(results):
        if len(r) > 0:
            jsonresults.append(json.loads(r))
    return jsonresults