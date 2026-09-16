def get_all(cls):
    issues = db.Issue.find(Issue.issue_type_id == IssueType.get(cls.
        issue_type).issue_type_id)
    return {res.issue_id: cls(res) for res in issues}