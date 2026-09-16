def wrap_response(resp, api_call):
    try:
        js_resp = resp.json()
        if resp.ok:
            if 'items' in js_resp.keys():
                r = ApiListResponse(js_resp['items'])
            else:
                r = ApiDictResponse(js_resp)
            if 'paging' in js_resp.keys():
                cursors = js_resp.get('paging', {}).get('cursors', {})
                if 'after' in cursors.keys():
                    r.next = api_call(after=cursors['after'])
                if 'before' in cursors.keys():
                    r.previous = api_call(after=cursors['before'])
        else:
            r = ApiDictResponse(js_resp)
            if 'error' in js_resp.keys():
                r.error = js_resp['error']
            elif 'message' in js_resp.keys():
                r.error = js_resp['message']
        r.status_code = resp.status_code
        r.headers = resp.headers
        return r
    except:
        return resp