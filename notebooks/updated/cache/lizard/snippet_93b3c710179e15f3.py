def earlier_submission_for_group(submission):
    return Submission.query_by(project=submission.project, group=submission
        .group).filter(Submission.created_at < submission.created_at).order_by(
        Submission.created_at.desc()).first()