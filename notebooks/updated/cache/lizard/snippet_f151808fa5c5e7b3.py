def show_warning_messages(self, title=_('Incorrect Operation'), box_type=
    'warning'):
    msg = self.current.task_data['msg']
    self.current.output['msgbox'] = {'type': box_type, 'title': title,
        'msg': msg}
    del self.current.task_data['msg']