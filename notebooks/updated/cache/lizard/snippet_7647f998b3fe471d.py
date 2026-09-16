def serialize(self):
    data = super(Note, self).serialize()
    data.update({'verb': 'post', 'object': {'objectType': self.object_type,
        'content': self.content}})
    if self.display_name:
        data['object']['displayName'] = self.display_name
    return data