def tarbell_install(command, args):
    with ensure_settings(command, args) as settings:
        project_url = args.get(0)
        puts('\n- Getting project information for {0}'.format(project_url))
        project_name = project_url.split('/').pop()
        error = None
        tempdir = tempfile.mkdtemp()
        try:
            testgit = sh.git.bake(_cwd=tempdir, _tty_in=True, _tty_out=False)
            testclone = testgit.clone(project_url, '.', '--depth=1', '--bare')
            puts(testclone)
            config = testgit.show('HEAD:tarbell_config.py')
            puts('\n- Found tarbell_config.py')
            path = _get_path(_clean_suffix(project_name, '.git'), settings)
            _mkdir(path)
            git = sh.git.bake(_cwd=path)
            clone = git.clone(project_url, '.', _tty_in=True, _tty_out=
                False, _err_to_out=True)
            puts(clone)
            puts(git.submodule.update('--init', '--recursive', _tty_in=True,
                _tty_out=False, _err_to_out=True))
            _install_requirements(path)
            with ensure_project(command, args, path) as site:
                site.call_hook('install', site, git)
        except sh.ErrorReturnCode_128 as e:
            if e.message.endswith('Device not configured\n'):
                error = """Git tried to prompt for a username or password.

Tarbell doesn't support interactive sessions. Please configure ssh key access to your Git repository. (See https://help.github.com/articles/generating-ssh-keys/)"""
            else:
                error = 'Not a valid repository or Tarbell project'
        finally:
            _delete_dir(tempdir)
            if error:
                show_error(error)
            else:
                puts('\n- Done installing project in {0}'.format(colored.
                    yellow(path)))