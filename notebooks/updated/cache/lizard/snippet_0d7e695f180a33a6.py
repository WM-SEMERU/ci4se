def get_event_data(self, section):
    event_group = '{}/BaseCalled_{}'.format(self.group_name, section)
    data = self.handle.get_analysis_dataset(event_group, 'Events')
    return data