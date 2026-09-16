def save_last_response_to_file(self, filename):
    response = self.get_last_response()
    return self.save_response_to_file(response, filename)