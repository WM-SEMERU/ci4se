def api(self):
    if self._api is None:
        from twilio.rest.api import Api
        self._api = Api(self)
    return self._api