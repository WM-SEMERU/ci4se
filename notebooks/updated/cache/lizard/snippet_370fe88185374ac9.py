def __update_information(self):
    info = {}
    info['actions_count'] = Action.objects.count()
    info['creation_times'] = []
    info['deletion_times'] = []
    info['content_type'] = None
    for ccommit in CreationCommit.objects.filter(object_uid=self.uid):
        info['creation_times'].append(ccommit.action.id)
    info['creation_times'].sort()
    for dcommit in DeletionCommit.objects.filter(object_uid=self.uid):
        info['deletion_times'].append(dcommit.action.id)
    info['deletion_times'].sort()
    try:
        info['content_type'] = ccommit.content_type
    except NameError:
        raise DisciplineException(
            "You tried to make a TimeMachine out of an object that doesn't exist!"
            )
    self.info = info
    for key in info.keys():
        setattr(self, key, info[key])