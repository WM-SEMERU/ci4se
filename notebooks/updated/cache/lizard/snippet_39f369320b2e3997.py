def set_rich_text_html(self, html_text, base_url):
    self.rich_text.set_html(html_text, base_url)
    self.save_text([self.rich_text.set_html, html_text, base_url])