def undo(self, editor):
    inst = self.timemachine
    if not self.is_revertible:
        raise DisciplineException(
            'You tried to undo a non-revertible action! Check action.is_revertible and action.undo_errors before trying to undo.'
            )
    if self.action_type == 'dl':
        obj = inst.restore()
        self.reverted = save_object(obj, editor)
        self.save()
    elif self.action_type == 'md':
        obj = inst.at_previous_action.restore()
        self.reverted = save_object(obj, editor)
        self.save()
    else:
        editor.delete_object(inst.get_object())
        self.reverted = DeletionCommit.objects.filter(object_uid=self.
            object_uid).order_by('-action__id')[0].action
        self.save()