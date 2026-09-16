def handle_starttag(self, tag, attrs):
    if tag in self.newline_before_elements:
        self.text += '\n'
    if tag in self.stroke_before_elements and not self.text.endswith(self.
        stroke_text):
        self.text += self.stroke_text
    if tag == 'a':
        for attr in attrs:
            if attr[0] == 'href':
                self.links.append((len(self.links) + 1, attr[1]))