def agree_to_tos(self, regr):
    return self.update_registration(regr.update(body=regr.body.update(
        agreement=regr.terms_of_service)))