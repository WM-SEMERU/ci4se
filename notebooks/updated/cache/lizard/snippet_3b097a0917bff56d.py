async def save(self):
    old_tags = list(self._orig_data['tags'])
    new_tags = list(self.tags)
    self._changed_data.pop('tags', None)
    await super(BlockDevice, self).save()
    for tag_name in new_tags:
        if tag_name not in old_tags:
            await self._handler.add_tag(system_id=self.node.system_id, id=
                self.id, tag=tag_name)
        else:
            old_tags.remove(tag_name)
    for tag_name in old_tags:
        await self._handler.remove_tag(system_id=self.node.system_id, id=
            self.id, tag=tag_name)
    self._orig_data['tags'] = new_tags
    self._data['tags'] = list(new_tags)