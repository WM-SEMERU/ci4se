def strip_mentions_links(self, text):
    new_text = [word for word in text.split() if not self.is_mention_line(word)
        ]
    return ' '.join(new_text)