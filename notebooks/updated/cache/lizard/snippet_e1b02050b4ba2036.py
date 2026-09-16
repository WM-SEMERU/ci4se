def onApprovalModeChange(self, mid=None, approval_mode=None, author_id=None,
    thread_id=None, thread_type=ThreadType.GROUP, ts=None, msg=None):
    if approval_mode:
        log.info('{} activated approval mode in {}'.format(author_id,
            thread_id))
    else:
        log.info('{} disabled approval mode in {}'.format(author_id, thread_id)
            )