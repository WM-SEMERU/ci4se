def get_unknown_topics(self, lang):
    return [topic['title'] for topic in self.user_data.language_data[lang][
        'skills'] if not topic['learned']]