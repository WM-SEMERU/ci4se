def handle_issue_comment(self, issue, title, body, **kwargs):
    if self._is_time_delta_valid(issue.updated_time_delta):
        if issue.comments_count < self.max_comments:
            issue.comment(body=body)
            return issue
        else:
            return self.create_issue(title=title, body=body, **kwargs)