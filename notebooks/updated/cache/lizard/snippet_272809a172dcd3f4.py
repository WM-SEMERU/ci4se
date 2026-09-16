def as_json(context):
    info = {'info': cgi.escape(pprint.pformat(context.context))}
    return Response(content_type='application/json', body=json.dumps(info))