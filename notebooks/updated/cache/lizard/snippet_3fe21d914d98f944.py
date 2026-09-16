def render_html(self):
    return self._template.safe_substitute(report_type=self._report_type,
        results=self.render_json())