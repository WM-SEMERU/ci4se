def _get_place_details(place_id, api_key, sensor=False, language=lang.ENGLISH):
    url, detail_response = _fetch_remote_json(GooglePlaces.DETAIL_API_URL,
        {'placeid': place_id, 'sensor': str(sensor).lower(), 'key': api_key,
        'language': language})
    _validate_response(url, detail_response)
    return detail_response['result']