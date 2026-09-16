def get_resource_tag_map(self, r_type, ids):
    manager = self.manager.get_resource_manager(r_type)
    r_id = manager.resource_type.id
    return {r[r_id]: {t['Key']: t['Value'] for t in r.get('Tags', [])} for
        r in manager.resources() if r[r_id] in ids}