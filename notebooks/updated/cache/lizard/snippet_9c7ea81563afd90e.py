def getscript(self, name):
    code, data, content = self.__send_command('GETSCRIPT', [name.encode(
        'utf-8')], withcontent=True)
    if code == 'OK':
        lines = content.splitlines()
        if self.__size_expr.match(lines[0]) is not None:
            lines = lines[1:]
        return '\n'.join([line.decode('utf-8') for line in lines])
    return None