def output(self, msg, indent, status=None):
    color = None
    if self.use_color:
        color = get_color_from_status(status)
    print_indent_msg(msg, indent, color)