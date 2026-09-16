def merge_into_group(self, group):
    super(VerboseMixin, self).merge_into_group(group)
    group.verbose_name = self.verbose_name
    group.help_text = self.help_text