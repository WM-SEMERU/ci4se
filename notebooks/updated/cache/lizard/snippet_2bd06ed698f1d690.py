def cmd(send, msg, args):
    if not msg:
        send('Calculate what?')
        return
    if '!' in msg:
        args['do_kick'](args['target'], args['nick'], 'hacking')
        return
    msg += '\n'
    proc = subprocess.Popen(['dc'], stdin=subprocess.PIPE, stdout=
        subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    try:
        output = proc.communicate(msg, timeout=5)[0].splitlines()
    except subprocess.TimeoutExpired:
        proc.terminate()
        send(
            'Execution took too long, you might have better luck with WolframAlpha.'
            )
        return
    if not output:
        send("No output found, did you forget to specify 'p'?")
    elif len(output) > 3:
        send('Your output is too long, have you tried mental math?')
    else:
        for line in output:
            send(line)