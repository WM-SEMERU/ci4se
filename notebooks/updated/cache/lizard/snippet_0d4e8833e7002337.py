def _generateGUID(slnfile, name):
    m = hashlib.md5()
    m.update(bytearray(ntpath.normpath(str(slnfile)) + str(name), 'utf-8'))
    solution = m.hexdigest().upper()
    solution = '{' + solution[:8] + '-' + solution[8:12] + '-' + solution[12:16
        ] + '-' + solution[16:20] + '-' + solution[20:32] + '}'
    return solution