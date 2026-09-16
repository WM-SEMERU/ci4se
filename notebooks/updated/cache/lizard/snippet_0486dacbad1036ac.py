def send_request(self, url):
    while True:
        try:
            return urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            raise serror('Request `%s` failed (%s:%s).' % (url, e.__class__
                .__name__, e.code))
        except Exception as e:
            choice = input(serror('Error occured: %s - Retry? [yN]' % type(e)))
            if choice.strip().lower() != 'y':
                raise serror(e)