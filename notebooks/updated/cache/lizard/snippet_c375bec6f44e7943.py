def _set_required_secrets(self, required_secrets, token_secrets):
    if self.user_params.build_type.value == BUILD_TYPE_ORCHESTRATOR:
        required_secrets += token_secrets
    if not required_secrets:
        return
    secrets = self.template['spec']['strategy']['customStrategy'].setdefault(
        'secrets', [])
    existing = set(secret_mount['secretSource']['name'] for secret_mount in
        secrets)
    required_secrets = set(required_secrets)
    already_set = required_secrets.intersection(existing)
    if already_set:
        logger.debug('secrets %s are already set', already_set)
    for secret in (required_secrets - existing):
        secret_path = os.path.join(SECRETS_PATH, secret)
        logger.info('Configuring %s secret at %s', secret, secret_path)
        secrets.append({'secretSource': {'name': secret}, 'mountPath':
            secret_path})