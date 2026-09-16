def get_datetime_issue_in_progress(self, issue):
    histories = issue.changelog.histories
    for history in reversed(histories):
        history_items = history.items
        for item in history_items:
            if item.field == 'status' and item.toString == 'In Progress':
                return dateutil.parser.parse(history.created)