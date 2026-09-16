def image_groups_list(self, limit=-1, offset=-1):
    return self.image_groups.list_objects(limit=limit, offset=offset)