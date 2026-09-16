def init_driver(client_id):
    profile_path = CHROME_CACHE_PATH + str(client_id)
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
    chrome_options = ['window-size=' + CHROME_WINDOW_SIZE,
        '--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'
        ]
    if CHROME_IS_HEADLESS:
        chrome_options.append('--headless')
    if CHROME_DISABLE_GPU:
        chrome_options.append('--disable-gpu')
    d = WhatsAPIDriver(username=client_id, profile=profile_path, client=
        'chrome', chrome_options=chrome_options)
    return d