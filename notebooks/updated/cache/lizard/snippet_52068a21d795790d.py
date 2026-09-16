def inclusion_tag(self, name, context_class=Context, takes_context=False):

    def tag_decorator(tag_func):

        @wraps(tag_func)
        def tag_wrapper(parser, token):


            class InclusionTagNode(template.Node):

                def render(self, context):
                    if not getattr(self, 'nodelist', False):
                        try:
                            request = context['request']
                        except KeyError:
                            t = get_template(name)
                        else:
                            ts = templates_for_device(request, name)
                            t = select_template(ts)
                        self.template = t
                    parts = [template.Variable(part).resolve(context) for
                        part in token.split_contents()[1:]]
                    if takes_context:
                        parts.insert(0, context)
                    result = tag_func(*parts)
                    autoescape = context.autoescape
                    context = context_class(result, autoescape=autoescape)
                    return self.template.render(context)
            return InclusionTagNode()
        return self.tag(tag_wrapper)
    return tag_decorator