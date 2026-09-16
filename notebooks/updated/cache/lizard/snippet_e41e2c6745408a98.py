def dependency_context(package_names, aggressively_remove=False):
    installed_packages = []
    log = logging.getLogger(__name__)
    try:
        if not package_names:
            logging.debug('No packages requested')
        if package_names:
            lock = yg.lockfile.FileLock('/tmp/.pkg-context-lock', timeout=
                30 * 60)
            log.info('Acquiring lock to perform install')
            lock.acquire()
            log.info('Installing ' + ', '.join(package_names))
            output = subprocess.check_output(['sudo', 'aptitude', 'install',
                '-y'] + package_names, stderr=subprocess.STDOUT)
            log.debug('Aptitude output:\n%s', output)
            installed_packages = jaraco.apt.parse_new_packages(output,
                include_automatic=aggressively_remove)
            if not installed_packages:
                lock.release()
            log.info('Installed ' + ', '.join(installed_packages))
        yield installed_packages
    except subprocess.CalledProcessError:
        log.error('Error occurred installing packages')
        raise
    finally:
        if installed_packages:
            log.info('Removing ' + ','.join(installed_packages))
            subprocess.check_call(['sudo', 'aptitude', 'remove', '-y'] +
                installed_packages, stdout=subprocess.PIPE, stderr=
                subprocess.STDOUT)
            lock.release()