def _validate_jpx_compatibility(self, boxes, compatibility_list):
    JPX_IDS = ['asoc', 'nlst']
    jpx_cl = set(compatibility_list)
    for box in boxes:
        if box.box_id in JPX_IDS:
            if len(set(['jpx ', 'jpxb']).intersection(jpx_cl)) == 0:
                msg = (
                    "A JPX box requires that either 'jpx ' or 'jpxb' be present in the ftype compatibility list."
                    )
                raise RuntimeError(msg)
        if hasattr(box, 'box') != 0:
            self._validate_jpx_compatibility(box.box, compatibility_list)