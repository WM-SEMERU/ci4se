def add_episode(self, text, text_format, title, author, summary=None,
    publish_date=None, synthesizer='watson', synth_args=None,
    sentence_break='. '):
    if title in self.episodes:
        raise ValueError('"' + title + '" already exists as an episode title.')
    link = self.output_path + '/' + title.replace(' ', '_').lower() + '.mp3'
    episode_text = convert_to_ssml(text, text_format)
    new_episode = Episode(episode_text, text_format, title, author, link,
        summary, publish_date, synthesizer, synth_args, sentence_break)
    self.episodes[title] = new_episode