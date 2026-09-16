def write_service_double_file(target_root, service_name, rendered):
    target_path = os.path.join(target_root, 'snapstore_schemas',
        'service_doubles', '%s.py' % service_name)
    with open(target_path, 'w') as target_file:
        target_file.write(rendered)