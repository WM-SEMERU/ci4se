def value(self):
    user = self.trigger.agentml.request_log.most_recent().user
    groups = self.trigger.agentml.request_log.most_recent().groups
    if len(self._element):
        message = ''.join(map(str, self.trigger.agentml.parse_tags(self.
            _element, self.trigger)))
    else:
        message = self._element.text
    default = attribute(self._element, 'default', '')
    response = self.trigger.agentml.get_reply(user.id, message, groups)
    return response or default