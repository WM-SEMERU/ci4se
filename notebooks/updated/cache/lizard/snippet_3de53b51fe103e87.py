def _cl_gof3r(file_info, region):
    command = ['gof3r', 'get', '--no-md5', '-k', file_info.key, '-b',
        file_info.bucket]
    if region != 'us-east-1':
        command += ['--endpoint=s3-%s.amazonaws.com' % region]
    return command, 'gof3r'