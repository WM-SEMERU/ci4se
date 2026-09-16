def get(cls, user_id, client_id, token_type='', access_token=None):
    args = [RemoteAccount.id == RemoteToken.id_remote_account, 
        RemoteAccount.user_id == user_id, RemoteAccount.client_id ==
        client_id, RemoteToken.token_type == token_type]
    if access_token:
        args.append(RemoteToken.access_token == access_token)
    return cls.query.options(db.joinedload('remote_account')).filter(*args
        ).first()