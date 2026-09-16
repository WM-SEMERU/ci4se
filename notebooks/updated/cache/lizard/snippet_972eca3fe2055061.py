def ApprovalGrant(token=None):
    user = getpass.getuser()
    notifications = GetNotifications(user=user, token=token)
    requests = [n for n in notifications if n.type == 'GrantAccess']
    for request in requests:
        _, client_id, user, reason = rdfvalue.RDFURN(request.subject).Split()
        reason = utils.DecodeReasonString(reason)
        print(request)
        print('Reason: %s' % reason)
        if input('Do you approve this request? [y/N] ').lower() == 'y':
            security.ClientApprovalGrantor(subject_urn=client_id, reason=
                reason, delegate=user, token=token).Grant()
        else:
            print('skipping request')
        print('Approval sent')