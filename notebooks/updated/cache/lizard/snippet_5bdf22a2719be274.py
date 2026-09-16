def run_setkey(input):
    SETKEY_BINARY = '/usr/sbin/setkey'
    fd, filename = tempfile.mkstemp('w')
    f = os.fdopen(fd, 'w')
    f.write(input)
    f.close()
    output = subprocess.check_output(['sudo', SETKEY_BINARY, '-f', filename])
    os.remove(filename)
    return output.decode('utf-8')