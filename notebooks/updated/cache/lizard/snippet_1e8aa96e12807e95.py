def _handle_presentation(self, msg):
    ret_msg = handle_presentation(msg)
    if msg.child_id == 255 or ret_msg is None:
        return
    topics = ['{}/{}/{}/{}/+/+'.format(self._in_prefix, str(msg.node_id),
        str(msg.child_id), msg_type) for msg_type in (int(self.const.
        MessageType.set), int(self.const.MessageType.req))]
    topics.append('{}/{}/+/{}/+/+'.format(self._in_prefix, str(msg.node_id),
        int(self.const.MessageType.stream)))
    self._handle_subscription(topics)