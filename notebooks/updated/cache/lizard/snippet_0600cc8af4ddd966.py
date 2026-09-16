def image_group_images_list(self, image_group_id, limit=-1, offset=-1):
    return self.image_groups.list_images(image_group_id, limit=limit,
        offset=offset)