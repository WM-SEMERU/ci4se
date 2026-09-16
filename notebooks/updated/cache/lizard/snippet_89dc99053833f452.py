def _add_video_timing(self, pic):
    sld = self._spTree.xpath('/p:sld')[0]
    childTnLst = sld.get_or_add_childTnLst()
    childTnLst.add_video(pic.shape_id)