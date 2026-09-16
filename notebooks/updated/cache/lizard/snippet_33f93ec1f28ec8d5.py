def get_description(self, lang='en'):
    if self.fast_run:
        return list(self.fast_run_container.get_language_data(self.
            wd_item_id, lang, 'description'))[0]
    if ('descriptions' not in self.wd_json_representation or lang not in
        self.wd_json_representation['descriptions']):
        return ''
    else:
        return self.wd_json_representation['descriptions'][lang]['value']