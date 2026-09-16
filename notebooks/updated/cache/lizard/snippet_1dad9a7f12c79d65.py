def browse_podcasts(self, podcast_genre_id='JZCpodcasttopchartall'):
    response = self._call(mc_calls.PodcastBrowse, podcast_genre_id=
        podcast_genre_id)
    podcast_series_list = response.body.get('series', [])
    return podcast_series_list