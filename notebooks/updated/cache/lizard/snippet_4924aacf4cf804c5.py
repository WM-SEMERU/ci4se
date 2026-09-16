def validate_href(image_href):
    try:
        response = requests.head(image_href)
        if response.status_code != http_client.OK:
            raise exception.ImageRefValidationFailed(image_href=image_href,
                reason=
                'Got HTTP code %s instead of 200 in response to HEAD request.'
                 % response.status_code)
    except requests.RequestException as e:
        raise exception.ImageRefValidationFailed(image_href=image_href,
            reason=e)
    return response