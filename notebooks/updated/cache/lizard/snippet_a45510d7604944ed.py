def add_token_to_database(encoded_token, identity_claim):
    decoded_token = decode_token(encoded_token)
    jti = decoded_token['jti']
    token_type = decoded_token['type']
    user_identity = decoded_token[identity_claim]
    expires = _epoch_utc_to_datetime(decoded_token['exp'])
    revoked = False
    db_token = TokenBlacklist(jti=jti, token_type=token_type, user_identity
        =user_identity, expires=expires, revoked=revoked)
    db.session.add(db_token)
    db.session.commit()