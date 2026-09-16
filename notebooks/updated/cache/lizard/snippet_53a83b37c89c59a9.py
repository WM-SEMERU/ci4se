async def deserialize(data: dict):
    try:
        credential_def = await CredentialDef._deserialize(
            'vcx_credentialdef_deserialize', json.dumps(data), data['data']
            ['source_id'], data['data']['name'], data['data']['id'])
        return credential_def
    except KeyError:
        raise VcxError(ErrorCode.InvalidCredentialDef)