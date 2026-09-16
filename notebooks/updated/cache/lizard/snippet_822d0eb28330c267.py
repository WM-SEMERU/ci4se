def get_changelog_date_packager(self):
    try:
        packager = subprocess.Popen('rpmdev-packager', stdout=subprocess.PIPE
            ).communicate()[0].strip()
    except OSError:
        packager = 'John Doe <john@doe.com>'
        logger.warn('Package rpmdevtools is missing, using default name: {0}.'
            .format(packager))
    with utils.c_time_locale():
        date_str = time.strftime('%a %b %d %Y', time.gmtime())
    encoding = locale.getpreferredencoding()
    return '{0} {1}'.format(date_str, packager.decode(encoding))