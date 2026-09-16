def delete_objects_associated_with_a_record(self, name, view, delete_list):
    search_objects = {}
    if 'record:cname' in delete_list:
        search_objects['record:cname'] = 'canonical'
    if 'record:txt' in delete_list:
        search_objects['record:txt'] = 'name'
    if not search_objects:
        return
    for obj_type, search_type in search_objects.items():
        payload = {'view': view, search_type: name}
        ib_objs = self.connector.get_object(obj_type, payload)
        if ib_objs:
            for ib_obj in ib_objs:
                self.delete_object_by_ref(ib_obj['_ref'])