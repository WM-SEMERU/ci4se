def monitor_mouse():
    import utool as ut
    import re
    import parse
    mouse_ids = ut.cmd('xinput --list ', verbose=False, quiet=True)[0]
    x = mouse_ids.decode('utf-8')
    pattern = 'mouse'
    pattern = 'trackball'
    print(x)
    grepres = ut.greplines(x.split('\n'), pattern, reflags=re.IGNORECASE)
    mouse_id = parse.parse('{left}id={id}{right}', grepres[0][0])['id']
    print('mouse_id = %r' % (mouse_id,))
    import time
    while True:
        time.sleep(0.2)
        out = ut.cmd('xinput --query-state ' + mouse_id, verbose=False,
            quiet=True)[0]
        print(out)