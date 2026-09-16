def sender(self, issues):
    for issue in issues:
        state = self.get_state(issue.state)
        if issue.number:
            try:
                gh_issue = self.repo.get_issue(issue.number)
                original_state = gh_issue.state
                if original_state == state:
                    action = 'Updated'
                elif original_state == 'closed':
                    action = 'Reopened'
                else:
                    action = 'Closed'
                gh_issue.edit(title=issue.title, body=issue.body, labels=
                    issue.labels, milestone=self.get_milestone(issue.
                    milestone), assignee=self.get_assignee(issue.assignee),
                    state=self.get_state(issue.state))
                print('{} #{}: {}'.format(action, gh_issue.number, gh_issue
                    .title))
            except GithubException:
                print('Not found #{}: {} (ignored)'.format(issue.number,
                    issue.title))
                continue
        else:
            gh_issue = self.repo.create_issue(title=issue.title, body=issue
                .body, labels=issue.labels, milestone=self.get_milestone(
                issue.milestone), assignee=self.get_assignee(issue.assignee))
            print('Created #{}: {}'.format(gh_issue.number, gh_issue.title))