def _get_section_start_index(self, section):
    sec_start_re = '%s\\s*\\{' % section
    found = re.search(sec_start_re, self.template_str)
    if found:
        return found.end() - 1
    raise NonextantSectionException('Section %s not found in template' %
        section)