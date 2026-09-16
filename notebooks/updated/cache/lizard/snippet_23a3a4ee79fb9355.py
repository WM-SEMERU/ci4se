def get_right_geo_fhs(self, dsid, fhs):
    ds_info = self.ids[dsid]
    req_geo, rem_geo = self._get_req_rem_geo(ds_info)
    desired, other = split_desired_other(fhs, req_geo, rem_geo)
    if desired:
        try:
            ds_info['dataset_groups'].remove(rem_geo)
        except ValueError:
            pass
        return desired
    else:
        return other