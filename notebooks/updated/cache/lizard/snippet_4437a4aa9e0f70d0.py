def pg_restore(self, pg_restore_exe='pg_restore', exclude_schema=None):
    command = [pg_restore_exe, '-d', 'service={}'.format(self.pg_service),
        '--no-owner']
    if exclude_schema:
        exclude_schema_available = False
        try:
            pg_version = subprocess.check_output(['pg_restore', '--version'])
            pg_version = str(pg_version).replace('\\n', '').replace("'", ''
                ).split(' ')[-1]
            exclude_schema_available = LooseVersion(pg_version
                ) >= LooseVersion('10.0')
        except subprocess.CalledProcessError as e:
            print('*** Could not get pg_restore version:\n', e.stderr)
        if exclude_schema_available:
            command.append(' '.join('--exclude-schema={}'.format(schema) for
                schema in exclude_schema))
    command.append(self.file)
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print('*** pg_restore failed:\n', command, '\n', e.stderr)