def get_registration_id_info(self, registration_id):
    response = self.registration_info_request(registration_id)
    if response.status_code == 200:
        return response.json()
    return None