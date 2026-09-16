def intent_verified(hub, callback_url, mode, topic_url, lease_seconds):
    challenge = uuid4()
    params = {'hub.mode': mode, 'hub.topic': topic_url, 'hub.challenge':
        challenge, 'hub.lease_seconds': lease_seconds}
    try:
        response = request_url(hub.config, 'GET', callback_url, params=params)
        assert response.status_code == 200 and response.text == challenge
    except requests.exceptions.RequestException as e:
        warn('Cannot verify subscriber intent', e)
    except AssertionError as e:
        warn(INTENT_UNVERIFIED % (response.status_code, response.content), e)
    else:
        return True
    return False