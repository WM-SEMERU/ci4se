def repository(namespace, name, branch='master'):
    with TemporaryDirectory() as download_path:
        old_directory = str(pwd()).strip()
        try:
            git.clone('https://github.com/{0}/{1}.git'.format(namespace,
                name), download_path)
            cd(download_path)
            git.fetch('origin', branch)
            git.checkout(branch)
            yield download_path, git('rev-parse', 'HEAD'), redis.Dict(key=
                '{0}.{1}'.format(namespace, name))
        except ErrorReturnCode_128:
            mkdir(download_path)
            yield None, None, None
        cd(old_directory)