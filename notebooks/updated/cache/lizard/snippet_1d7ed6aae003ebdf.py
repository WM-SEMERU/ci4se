def build(self, response):
    response_json = response.json()
    if get_endpoint_path(self.api, response).startswith('/ticket_audits.json'):
        return TicketAuditGenerator(self, response_json)
    zenpy_objects = self.deserialize(response_json)
    plural_object_type = as_plural(self.api.object_type)
    if plural_object_type in zenpy_objects:
        return ZendeskResultGenerator(self, response_json, response_objects
            =zenpy_objects[plural_object_type])
    if self.api.object_type in zenpy_objects:
        return zenpy_objects[self.api.object_type]
    for zenpy_object_name in self.object_mapping.class_mapping:
        if zenpy_object_name in zenpy_objects:
            return zenpy_objects[zenpy_object_name]
    for zenpy_object_name in self.object_mapping.class_mapping:
        plural_zenpy_object_name = as_plural(zenpy_object_name)
        if plural_zenpy_object_name in zenpy_objects:
            return ZendeskResultGenerator(self, response_json, object_type=
                plural_zenpy_object_name)
    raise ZenpyException('Unknown Response: ' + str(response_json))