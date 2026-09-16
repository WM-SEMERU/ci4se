def output(stream):
    while True:
        content = stream.read(1024)
        if len(content) == 0:
            break
        sys.stdout.write(content)