def experiments_create(self, subject_id, image_group_id, properties):
    if self.subjects_get(subject_id) is None:
        raise ValueError('unknown subject: ' + subject_id)
    if self.image_groups_get(image_group_id) is None:
        raise ValueError('unknown image group: ' + image_group_id)
    return self.experiments.create_object(subject_id, image_group_id,
        properties)