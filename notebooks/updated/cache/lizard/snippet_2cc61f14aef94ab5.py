def parse(self, text):
    self._parsed_list = []
    self._most_recent_report = []
    self._token_list = text.lower().split()
    modifier_index_list = []
    for item in self._token_list:
        if self._is_token_data_callback(item):
            self._parsed_list.append(self._clean_data_callback(item))
        if item in self._tasks:
            d = {}
            d['context'] = self._tasks[item]['context']
            d['rule'] = self._tasks[item]['rule']
            d['task'] = item
            self._parsed_list.append(d)
        if item in self._modifiers:
            modifier_index_list.append((len(self._parsed_list), item))
    self._apply_modifiers(modifier_index_list)
    return self._evaluate()