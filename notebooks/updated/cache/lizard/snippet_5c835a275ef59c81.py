def send(self, group_id=None, message_dict=None):
    if self.group is not None and self.group.id is not None:
        group_id = self.group.id
    path = 'message/%s' % group_id
    if message_dict is not None:
        request_data = {'message': message_dict}
    else:
        subject = self.subject
        text = self.text
        markdown = self.markdown
        request_data = {'message': {}}
        if subject:
            request_data['message']['subject'] = subject
        if text:
            request_data['message']['text'] = text
        if markdown:
            request_data['message']['markdown'] = markdown
    response_data = self.api.request(path, request_data)
    self.id = response_data['message_id']
    self.thread_id = response_data['thread_id']
    self.sent_message = FiestaMessage(self.api, response_data['message'])