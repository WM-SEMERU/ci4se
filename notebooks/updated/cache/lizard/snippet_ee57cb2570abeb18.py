def _parse_response(self, response, target_object=strack):
    objects = json.loads(response.read().decode('utf-8'))
    list = []
    for obj in objects:
        list.append(target_object(obj, client=self.client))
    return list