def from_commit_msg(commit_msg_str):
    context = GitContext()
    commit_msg_obj = GitCommitMessage.from_full_message(commit_msg_str)
    commit = GitCommit(context, commit_msg_obj)
    context.commits.append(commit)
    return context