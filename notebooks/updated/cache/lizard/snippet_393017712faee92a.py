def render_json_response(self, context_dict, status=200):
    json_context = json.dumps(context_dict, cls=DjangoJSONEncoder, **self.
        get_json_dumps_kwargs()).encode('utf-8')
    return HttpResponse(json_context, content_type=self.get_content_type(),
        status=status)