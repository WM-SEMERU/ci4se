def get_type(self):
    mtype = None
    if 'type' not in self.meta_data:
        return mtype
    mtype = self.meta_data['type']
    if isinstance(mtype, dict):
        mtype = self.meta_data.get('type', {}).get('name', '').upper()
    elif isinstance(mtype, str):
        mtype = mtype
    return mtype