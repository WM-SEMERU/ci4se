def parse_tag_groups(self):
    tag_groups = []
    if 'tag_groups' not in self._device_dict:
        return tag_groups
    to_remove = []
    for tag_group in self._device_dict['tag_groups']:
        if tag_group['common.ALLTYPES_NAME'] in self._ignore_list:
            to_remove.append(tag_group)
            continue
        tag_groups.append(TagGroup(tag_group))
    for removable in to_remove:
        self._device_dict['tag_groups'].remove(removable)
    return tag_groups