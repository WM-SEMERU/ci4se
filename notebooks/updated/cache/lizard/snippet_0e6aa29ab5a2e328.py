def find_response_component(self, api_id=None, signature_id=None):
    if not api_id and not signature_id:
        raise ValueError('At least one of api_id and signature_id is required')
    components = list()
    if self.response_data:
        for component in self.response_data:
            if (api_id and component['api_id']
                ) == api_id or signature_id and component['signature_id'
                ] == signature_id:
                components.append(component)
    return components