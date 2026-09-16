def get_athlete(self, athlete_id=None):
    if athlete_id is None:
        raw = self.protocol.get('/athlete')
    else:
        raise NotImplementedError(
            'The /athletes/{id} endpoint was removed by Strava.  See https://developers.strava.com/docs/january-2018-update/'
            )
    return model.Athlete.deserialize(raw, bind_client=self)