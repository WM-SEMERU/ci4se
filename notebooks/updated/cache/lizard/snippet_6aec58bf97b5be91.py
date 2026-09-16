def add_issue(self, subject, priority, status, issue_type, severity, **attrs):
    return Issues(self.requester).create(self.id, subject, priority, status,
        issue_type, severity, **attrs)