def serialize_encrypted_data_key(encrypted_data_key):
    encrypted_data_key_format = (
        '>H{provider_id_len}sH{provider_info_len}sH{enc_data_key_len}s')
    return struct.pack(encrypted_data_key_format.format(provider_id_len=len
        (encrypted_data_key.key_provider.provider_id), provider_info_len=
        len(encrypted_data_key.key_provider.key_info), enc_data_key_len=len
        (encrypted_data_key.encrypted_data_key)), len(encrypted_data_key.
        key_provider.provider_id), to_bytes(encrypted_data_key.key_provider
        .provider_id), len(encrypted_data_key.key_provider.key_info),
        to_bytes(encrypted_data_key.key_provider.key_info), len(
        encrypted_data_key.encrypted_data_key), encrypted_data_key.
        encrypted_data_key)