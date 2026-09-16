def get_all(cls, account=None, location=None, include_disabled=False):
    qry = db.Resource.filter(Resource.resource_type_id == ResourceType.get(
        cls.resource_type).resource_type_id)
    if account:
        qry = qry.filter(Resource.account_id == account.account_id)
    if not include_disabled:
        qry = qry.join(Account, Resource.account_id == Account.account_id
            ).filter(Account.enabled == 1)
    if location:
        qry = qry.filter(Resource.location == location)
    return {res.resource_id: cls(res) for res in qry.all()}