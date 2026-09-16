def data(self, data):
    if self.state == STATE_SOURCE_ID:
        self.context.audit_record.source_id = int(data)
    elif self.state == STATE_DATETIME:
        dt = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')
        self.get_parent_element().datetimestamp = dt
    elif self.state == STATE_REASON_FOR_CHANGE:
        self.context.audit_record.reason_for_change = data.strip() or None
    self.state = STATE_NONE