def create_swagger_json_handler(app, **kwargs):
    spec = get_swagger_spec(app).swagger_definition(**kwargs)
    encoded_spec = json.dumps(spec).encode('UTF-8')

    async def swagger(request):
        return web.Response(headers={'Access-Control-Allow-Origin': '*'},
            body=encoded_spec, content_type='application/json')
    return swagger