def PackageUpload(package, ftp_url):
    if not os.path.isfile(package):
        clc.v1.output.Status('ERROR', 2, 'Package file (%s) not found' %
            package)
        return
    m = re.search('ftp://(?P<user>.+?):(?P<passwd>.+?)@(?P<host>.+)', ftp_url)
    try:
        ftp = ftplib.FTP(m.group('host'), m.group('user'), m.group('passwd'))
        file = open(package, 'rb')
        filename = re.sub('.*/', '', package)
        ftp.storbinary('STOR %s' % filename, file)
        file.close()
        ftp.quit()
        clc.v1.output.Status('SUCCESS', 2, 'Blueprint package %s Uploaded' %
            filename)
    except Exception as e:
        clc.v1.output.Status('ERROR', 2, 'FTP error %s: %s' % (ftp_url, str(e))
            )
    return {}