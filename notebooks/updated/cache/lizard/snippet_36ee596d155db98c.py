def get_club(self, club_id):
    raw = self.protocol.get('/clubs/{id}', id=club_id)
    return model.Club.deserialize(raw, bind_client=self)