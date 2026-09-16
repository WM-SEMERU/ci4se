def project_activity(index, start, end):
    results = {'metrics': [OpenedIssues(index, start, end), ClosedIssues(
        index, start, end)]}
    return results