def _watch_travis_build(build_id):
    import requests
    try:
        build_size = None
        running = True
        while running:
            with requests.get('https://api.travis-ci.org/builds/%d' %
                build_id, headers=_travis_headers()) as r:
                json = r.json()
                if build_size is not None:
                    if build_size > 1:
                        sys.stdout.write('\r\x1b[%dA' % build_size)
                    else:
                        sys.stdout.write('\r')
                build_size = len(json['jobs'])
                running = False
                current_number = 1
                for job in json['jobs']:
                    color, state, is_running = _travis_job_state(job['state'])
                    if is_running:
                        running = True
                    platform = job['config']['os']
                    if platform == 'osx':
                        platform = ' osx '
                    env = job['config'].get('env', '')
                    sudo = 's' if job['config'].get('sudo', True) else 'c'
                    lang = job['config'].get('language', 'generic')
                    padding = ' ' * (len(str(build_size)) - len(str(
                        current_number)))
                    number = str(current_number) + padding
                    current_number += 1
                    job_display = '#' + ' '.join([number, state, platform,
                        sudo, lang, env])
                    print(color + job_display + colorama.Style.RESET_ALL)
            time.sleep(3.0)
    except KeyboardInterrupt:
        pass