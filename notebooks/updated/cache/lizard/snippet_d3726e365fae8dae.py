def handle_message(self, msg):
    if msg.msg_id not in self.msg_types:
        self.report_message_type(msg)
        self.msg_types.add(msg.msg_id)
    self.tc.message('inspection', typeId=msg.msg_id, message=msg.msg, file=
        os.path.relpath(msg.abspath).replace('\\', '/'), line=str(msg.line),
        SEVERITY=TC_SEVERITY.get(msg.category))