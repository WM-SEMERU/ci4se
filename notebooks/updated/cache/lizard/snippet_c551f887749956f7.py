def get_email_logs(self):
    message = ''
    for log in self.record:
        if log['log_type'] in [ERROR, WARNING]:
            message += self.format_message(**log)
    return message