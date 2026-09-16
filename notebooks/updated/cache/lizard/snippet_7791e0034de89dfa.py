def parse_plays_stream(self):
    lx_doc = self.html_doc()
    if lx_doc is not None:
        parser = PlayParser(self.game_key.season, self.game_key.game_type)
        plays = lx_doc.xpath('//tr[@class = "evenColor"]')
        for p in plays:
            p_obj = parser.build_play(p)
            self.plays.append(p_obj)
            yield p_obj