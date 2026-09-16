def should_show_thanks_page_to(participant):
    if participant is None:
        return False
    status = participant.status
    marked_done = participant.end_time is not None
    ready_for_external_submission = status in ('overrecruited', 'working'
        ) and marked_done
    assignment_complete = status in ('submitted', 'approved')
    return assignment_complete or ready_for_external_submission