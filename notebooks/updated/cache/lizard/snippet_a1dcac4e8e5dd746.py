def _description(self):
    inst = self.timemachine.presently
    if self.action_type == 'dl':
        return 'Deleted %s' % inst.content_type.name
    elif self.action_type == 'cr':
        return 'Created %s' % inst._object_type_html()
    else:
        return 'Modified %s' % inst._object_type_html()