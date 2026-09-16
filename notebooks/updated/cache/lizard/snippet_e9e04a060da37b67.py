def put(self):
    cred_payload = utils.uni_to_str(json.loads(request.get_data()))
    return self.manager.update_credential(cred_payload)