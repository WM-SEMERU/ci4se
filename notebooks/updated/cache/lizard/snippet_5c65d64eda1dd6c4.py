def get_stores_secrets_volumes(cls, stores_secrets):
    volumes = []
    volume_mounts = []
    for store_secret in stores_secrets:
        store = store_secret['store']
        if store in {GCS, S3}:
            secrets_volumes, secrets_volume_mounts = get_volume_from_secret(
                volume_name=cls.STORE_SECRET_VOLUME_NAME.format(store),
                mount_path=cls.STORE_SECRET_KEY_MOUNT_PATH.format(store),
                secret_name=store_secret['persistence_secret'])
            volumes += secrets_volumes
            volume_mounts += secrets_volume_mounts
    return volumes, volume_mounts