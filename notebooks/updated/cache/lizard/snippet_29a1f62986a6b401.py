def CheckApprovalRequest(approval_request):
    at = rdf_objects.ApprovalRequest.ApprovalType
    if approval_request.approval_type == at.APPROVAL_TYPE_CLIENT:
        return CheckClientApprovalRequest(approval_request)
    elif approval_request.approval_type == at.APPROVAL_TYPE_HUNT:
        return CheckHuntApprovalRequest(approval_request)
    elif approval_request.approval_type == at.APPROVAL_TYPE_CRON_JOB:
        return CheckCronJobApprovalRequest(approval_request)
    else:
        raise ValueError('Invalid approval type: %s' % approval_request.
            approval_type)