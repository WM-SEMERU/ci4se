def get(self, country_code):
    return AvailablePhoneNumberCountryContext(self._version, account_sid=
        self._solution['account_sid'], country_code=country_code)