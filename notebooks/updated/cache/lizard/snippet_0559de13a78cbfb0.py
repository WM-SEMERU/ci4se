def get_languages(self, abbreviations=False):
    data = []
    for lang in self.user_data.languages:
        if lang['learning']:
            if abbreviations:
                data.append(lang['language'])
            else:
                data.append(lang['language_string'])
    return data