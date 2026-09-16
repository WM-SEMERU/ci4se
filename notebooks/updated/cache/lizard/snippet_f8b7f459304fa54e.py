def parse_away_face_offs(self):
    self.__set_team_docs()
    self.face_offs['away'] = FaceOffRep.__read_team_doc(self.__vis_doc)
    return self