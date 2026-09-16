def _form_pages(self, message_no, content, out, height, width):
    self.pages[message_no] = []
    page_height = height - 4
    outline = ''
    no_lines_page = 0
    for original, formatted in zip(content.split('\n'), out.split('\n')):
        no_lines_original = int(math.ceil(len(original) / float(width)))
        if len(original) == 0:
            if no_lines_page + 1 <= page_height:
                outline += '\n'
                no_lines_page += 1
            else:
                self.pages[message_no].append(outline)
                outline = '\n'
                no_lines_page = 1
            original = formatted = '\n'
        elif no_lines_original > page_height:
            if len(outline) > 0:
                self.pages[message_no].append(outline)
                outline = ''
                no_lines_page = 0
            self.pages[message_no].append(formatted)
        elif no_lines_page + no_lines_original <= page_height:
            if len(outline) > 0:
                outline += '\n'
            outline += formatted
            no_lines_page += no_lines_original
        else:
            self.pages[message_no].append(outline)
            outline = formatted
            no_lines_page = no_lines_original
    if len(outline) > 0:
        self.pages[message_no].append(outline)
    if len(self.pages[message_no]) == 0:
        self.pages[message_no].append('')