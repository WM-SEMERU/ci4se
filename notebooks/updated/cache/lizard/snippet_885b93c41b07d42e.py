def _update_local_conf(config, service_id, client_secret):
    lines = _get_existing_conf(config)
    lines.append('\nservice_id = "{}"\n'.format(service_id))
    if client_secret:
        lines.append('client_secret = "{}"\n'.format(client_secret))
    with open(os.path.join(config, 'local.conf'), 'w') as f:
        f.writelines(lines)