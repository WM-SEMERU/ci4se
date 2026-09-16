def get_reply_visibility(self, status_dict):
    visibility = 'public', 'unlisted', 'private', 'direct'
    default_visibility = visibility.index(self.default_visibility)
    status_visibility = visibility.index(status_dict['visibility'])
    return visibility[max(default_visibility, status_visibility)]