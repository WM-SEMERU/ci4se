def instagram_scrap_profile(username):
    try:
        url = 'https://www.instagram.com/{}/'.format(username)
        page = requests.get(url)
        page.raise_for_status()
        return html.fromstring(page.content)
    except HTTPError:
        logging.exception('user profile "{}" not found'.format(username))
    except (ConnectionError, socket_error) as e:
        logging.exception('instagram.com unreachable')