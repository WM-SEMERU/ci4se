def prog_callback(prog, msg):
    pipe = Popen(prog, stdin=PIPE)
    data = json.dumps(msg)
    pipe.stdin.write(data.encode('utf-8'))
    pipe.stdin.close()