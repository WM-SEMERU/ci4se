def groff2man(data):
    width = get_width()
    cmd = 'groff -t -Tascii -m man -rLL=%dn -rLT=%dn' % (width, width)
    handle = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    man_text, stderr = handle.communicate(data)
    return man_text