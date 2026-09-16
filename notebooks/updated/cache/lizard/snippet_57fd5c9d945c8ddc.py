def phoneid(self, phone_number, **params):
    return self.post(PHONEID_RESOURCE.format(phone_number=phone_number), **
        params)