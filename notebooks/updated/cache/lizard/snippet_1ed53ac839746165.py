def can_approve(self, user, **data):
    service_id = data.get('service_id', self.service_id)
    try:
        service = yield Service.get(service_id)
        is_repo_admin = user.is_org_admin(service.organisation_id)
        is_reseller_preverifying = user.is_reseller() and data.get(
            'pre_verified', False)
        raise Return(is_repo_admin or is_reseller_preverifying)
    except couch.NotFound:
        pass
    raise Return(False)