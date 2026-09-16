def player_s(self, sid):
    try:
        url = self.pubg_url_steam.format(str(sid))
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)
    except BaseException as error:
        print('Unhandled exception: ' + str(error))
        raise