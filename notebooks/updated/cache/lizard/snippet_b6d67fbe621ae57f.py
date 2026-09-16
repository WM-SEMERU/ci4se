def delete_place(self, place_id, sensor=False):
    request_params = {'place_id': place_id}
    url, delete_response = _fetch_remote_json(GooglePlaces.DELETE_API_URL %
        (str(sensor).lower(), self.api_key), json.dumps(request_params),
        use_http_post=True)
    _validate_response(url, delete_response)