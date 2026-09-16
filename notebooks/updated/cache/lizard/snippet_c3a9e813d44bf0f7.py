def save_logic(self, some_object):
    some_object.validate_model()
    some_object.save()
    self.send_success_response(data=some_object.to_dict())