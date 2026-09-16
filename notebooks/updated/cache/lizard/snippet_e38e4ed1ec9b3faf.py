def get_content_json(request):
    result = _get_content_json()
    resp = request.response
    resp.status = '200 OK'
    resp.content_type = 'application/json'
    resp.body = json.dumps(result)
    return result, resp