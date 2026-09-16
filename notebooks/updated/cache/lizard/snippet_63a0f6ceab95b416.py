def commit(self):
    obj = self.object
    while obj.type != 'commit':
        if obj.type == 'tag':
            obj = obj.object
        else:
            raise ValueError((
                'Cannot resolve commit as tag %s points to a %s object - ' +
                'use the `.object` property instead to access it') % (self,
                obj.type))
    return obj