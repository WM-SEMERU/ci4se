def metadata(access_token, text):
    headers = {'Content-Type': 'application/json', 'Authorization': 
        'Bearer ' + str(access_token)}
    payload = {'text': text}
    request = requests.post(metadata_url, json=payload, headers=headers)
    if request.status_code == 201:
        metadata = request.json()
        return metadata
    return {'status': request.status_code, 'message': request.text}