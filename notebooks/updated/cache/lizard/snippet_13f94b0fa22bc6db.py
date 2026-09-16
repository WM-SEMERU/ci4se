def write_base(self, url_data):
    self.writeln('<tr><td>' + self.part('base') + '</td><td>' + cgi.escape(
        url_data.base_ref) + '</td></tr>')