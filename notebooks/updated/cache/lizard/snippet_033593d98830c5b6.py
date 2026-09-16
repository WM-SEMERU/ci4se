def replace_uuid_w_names(self, resp):
    col_mapper = self.get_point_name(resp.context)['?point'].to_dict()
    resp.df.rename(columns=col_mapper, inplace=True)
    return resp