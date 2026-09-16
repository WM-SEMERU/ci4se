def runcode(code):
    for line in code:
        print('# ' + line)
        exec(line, globals())
    print('# return ans')
    return ans