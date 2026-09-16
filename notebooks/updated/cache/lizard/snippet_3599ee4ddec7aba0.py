def update(self):
    if self._is_ignored or 'tags' not in self._tag_group_dict:
        return
    for i in range(len(self._tag_group_dict['tags'])):
        tag_dict = self._tag_group_dict['tags'][i]
        for tag in self._tags:
            if tag.name == tag_dict['common.ALLTYPES_NAME']:
                self._tag_group_dict['tags'][i] = tag.as_dict()
                break
    for i in range(len(self._sub_groups)):
        sub_group = self._sub_groups[i]
        sub_group.update()
        self._tag_group_dict['tag_groups'][i] = sub_group.as_dict()