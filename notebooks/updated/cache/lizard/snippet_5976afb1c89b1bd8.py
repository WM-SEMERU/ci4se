def template(self):
    r = fapi.get_config_template(self.namespace, self.name, self.
        snapshot_id, self.api_url)
    fapi._check_response_code(r, 200)
    return r.json()