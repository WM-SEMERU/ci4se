def render_tag(self, tag_func):

    @wraps(tag_func)
    def tag_wrapper(parser, token):


        class RenderTagNode(template.Node):

            def render(self, context):
                return tag_func(context, token)
        return RenderTagNode()
    return self.tag(tag_wrapper)