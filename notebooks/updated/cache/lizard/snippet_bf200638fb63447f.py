def write_dltime(self, url_data):
    self.writeln('<tr><td>' + self.part('dltime') + '</td><td>' + _(
        '%.3f seconds') % url_data.dltime + '</td></tr>')