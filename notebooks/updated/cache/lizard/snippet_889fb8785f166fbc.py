def set_from_match(self, key, regex_list, string):
    for item in regex_list:
        if hasattr(item, '__call__'):
            self.set(key, *item(string))
        else:
            regex, value, confidence = item
            if regex.search(string):
                self.set(key, value, confidence)