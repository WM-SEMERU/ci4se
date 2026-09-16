def _make_spec_file(self):
    spec_file = setuptools.command.bdist_rpm.bdist_rpm._make_spec_file(self)
    spec_file.append('%config(noreplace) /etc/lograptor/lograptor.conf')
    spec_file.append('%config(noreplace) /etc/lograptor/report_template.*')
    spec_file.append('%config(noreplace) /etc/lograptor/conf.d/*.conf')
    return spec_file